import conection_mysql
from flask import Flask,jsonify,request

app = Flask (__name__)


@app.route('/api/ingresos', methods=['GET'])

def read():
    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql= "SELECT IngresosId,Fecha,Concepto,Monto,Metodo_ingreso,cuenta_ingreso,Descripcion,UserId FROM ingresos;"
                cursor.execute(sql)
                results = cursor.fetchall()
                ingresos_data = []
                for row in results:
                    ingresos_data.append({'Ingresos Id': row['IngresosId'], 'Fecha': row['Fecha'], 'Concepto': row['Concepto'], 'Monto': row['Monto'], 'Metodo_ingreso': row['Metodo_ingreso'],
                                        'Cuenta_ingreso': row['Cuenta_ingreso'], 'Descripcion': row['Descripcion']})
                return jsonify({'data': ingresos_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    

@app.route('/api/ingresos', methods=['POST'])

def create():
    
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql= "INSERT IN TO ingresos (Concepto,Monto,Metodo_ingreso,cuenta_ingreso,Descripcion) SET VALUES(%s, %s, %s, %s,%s, %s);"
                cursor.execute(sql, (data['Concepto'], data['Monto'], data['Metodo_ingreso'], data['cuenta_ingreso'], data['Descripcion']))
                connection.commit()
        return jsonify({'message': 'Successful creation'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    


    
