import conection_mysql
from flask import Flask, jsonify

app = Flask(__name__)

def get_all_data_users():
    try:
        connection = conection_mysql.conectar()
        if connection is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT Nombre, Saldo_disponible_inicial, TotalIngresos, TotalGastos, SaldoActual FROM usuarios JOIN dashboard ON usuarios.UsuarioId = dashboard.UsuarioId;'
                cursor.execute(sql)
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({
                        'Nombre': row['Nombre'],
                        'Saldo Incial': row['Saldo_disponible_inicial'],
                        'Total de Ingresos': row['TotalIngresos'],
                        'Total de Gastos': row['TotalGastos'],
                        'Saldo Actual': row['SaldoActual']
                    })
                return jsonify({'data_finanzas': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Solicitar los datos de dashboard por numero de cedula

def get_one_user_dashboard(cedula):
    try:
        connection = conection_mysql.conectar()
        if connection is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500
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
                result = cursor.fetchone()

                if result:
                    return jsonify({'data': result}), 200
                else:
                    return jsonify({'message': 'Usuario no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
