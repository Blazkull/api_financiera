import conection_mysql
from flask import Flask, jsonify, request


app = Flask(__name__)






@app.route('/api/users', methods=['GET'])
def read():
    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT UsuarioId, Nombre, Edad, Cedula, Telefono, Saldo_disponible_inicial FROM usuarios'
                cursor.execute(sql)
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({'Usuario Id': row['UsuarioId'], 'Nombre': row['Nombre'], 'Edad': row['Edad'], 'Cedula': row['Cedula'], 'Telefono': row['Telefono'], 'Saldo Inicial': row['Saldo_disponible_inicial']})
                return jsonify({'data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/users', methods=['POST'])
def create():
    try:
       
        data = request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Invalid request data'}), 400


        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO usuarios (Nombre, Edad, Cedula, Telefono, Saldo_disponible_inicial) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (data['Nombre'], data['Edad'], data['Cedula'], data['Telefono'], data['Saldo_disponible_inicial']))
            connection.commit()
        return jsonify({'message': 'Successful creation'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)