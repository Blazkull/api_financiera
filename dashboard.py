import conection_mysql
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/dashboard', methods=['GET'])
def read():
    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT u.Nombre, u.Saldo_disponible_inicial,d.TotalIngresos,d.TotalGastos,d.SaldoActual FROM usuarios u JOIN dashboard d ON u.UsuarioId = d.UsuarioId;'
                cursor.execute(sql)
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({'Nombre': row['u.Nombre'], 'Saldo Incial': row['u.Saldo_disponible_inicial'], 'Total de Ingresos': row['d.TotalIngresos'], 'Total de Gastos': row['d.TotalGastos'], 'Saldo Actual': row['d.SaldoActual']})
                return jsonify({'data_finanzas': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/users/dashboard/<int:cedula>', methods=['GET'])
def get_user_dashboard(cedula):
    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor: 
                sql = """
                    SELECT
                        u.Nombre,
                        d.TotalIngresos,
                        d.TotalGastos,
                        d.SaldoActual
                    FROM
                        usuarios u
                    JOIN
                        dashboard d ON u.UsuarioId = d.UsuarioId
                    WHERE
                        u.Cedula = %s
                """
                cursor.execute(sql, (cedula,))
                row = cursor.fetchone()

                if row:
                    # Convertir el resultado en un diccionario manualmente
                    column_names = [desc[0] for desc in cursor.description]
                    result = dict(zip(column_names, row))
                    return jsonify({'data': result}), 200
                else:
                    return jsonify({'message': 'Usuario no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)