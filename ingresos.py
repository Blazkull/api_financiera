from flask import Flask, jsonify, request
import conection_mysql

app = Flask(__name__)

# Método GET: Obtener todos los ingresos

def get_all_ingresos():
    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT IngresosId, Fecha, Concepto, Monto, Metodo_ingreso, Cuenta_ingreso, Descripcion, UserId FROM ingresos;"
                cursor.execute(sql)
                results = cursor.fetchall()
                ingresos_data = [
                    {'IngresosId': row['IngresosId'], 'Fecha': row['Fecha'], 'Concepto': row['Concepto'], 'Monto': row['Monto'],
                     'Metodo_ingreso': row['Metodo_ingreso'], 'Cuenta_ingreso': row['Cuenta_ingreso'], 'Descripcion': row['Descripcion'], 'UserId': row['UserId']}
                    for row in results
                ]
                return jsonify({'data': ingresos_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Método POST: Crear un nuevo ingreso (requiere UserId existente en usuarios)

def crete_insert():
    try:
        data = request.get_json()
        if not data or 'fecha' not in data or 'concepto' not in data or 'monto' not in data or 'metodo_ingreso' not in data or 'cuenta_ingreso' not in data or 'descripcion' not in data or 'UserId' not in data:
            return jsonify({'error': 'Datos inválidos'}), 400

        connection = conection_mysql.conectar()
        if connection is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

        with connection:
            with connection.cursor() as cursor:
                # Verificar si el UserId existe
                sql_check_user = "SELECT UsuarioId FROM usuarios WHERE UsuarioId = %s;"
                cursor.execute(sql_check_user, (data['UserId'],))
                user_exists = cursor.fetchone()

                if not user_exists:
                    return jsonify({'error': 'El usuario no existe'}), 400

                # Insertar el ingreso si el UserId es válido
                sql_insert = """INSERT INTO ingresos (Fecha, Concepto, Monto, Metodo_ingreso, Cuenta_ingreso, Descripcion, UserId) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                cursor.execute(sql_insert, (data['fecha'], data['concepto'], data['monto'], data['metodo_ingreso'], data['cuenta_ingreso'], data['descripcion'], data['UserId']))
                connection.commit()

        return jsonify({'message': 'Ingreso creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Método PUT: Actualizar un ingreso por ID (verifica UserId válido)

def update_insert__of_user(IngresosId):
    try:
        data = request.get_json()
        if not data or 'fecha' not in data or 'concepto' not in data or 'monto' not in data or 'metodo_ingreso' not in data or 'cuenta_ingreso' not in data or 'descripcion' not in data or 'UserId' not in data:
            return jsonify({'error': 'Datos inválidos'}), 400

        connection = conection_mysql.conectar()
        if connection is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

        with connection:
            with connection.cursor() as cursor:
                # Verificar si el ingreso existe
                sql_check_ingreso = "SELECT IngresosId FROM ingresos WHERE IngresosId = %s;"
                cursor.execute(sql_check_ingreso, (IngresosId,))
                ingreso_exists = cursor.fetchone()

                if not ingreso_exists:
                    return jsonify({'error': 'El ingreso con el ID proporcionado no existe'}), 404

                # Verificar si el UserId existe en la tabla usuarios
                sql_check_user = "SELECT UsuarioId FROM usuarios WHERE UsuarioId = %s;"
                cursor.execute(sql_check_user, (data['UserId'],))
                user_exists = cursor.fetchone()

                if not user_exists:
                    return jsonify({'error': 'El usuario no existe'}), 400

                # Si existe, actualizarlo
                sql_update = """UPDATE ingresos 
                                    SET Fecha = %s, Concepto = %s, Monto = %s, Metodo_ingreso = %s, Cuenta_ingreso = %s, Descripcion = %s, UserId = %s 
                                    WHERE IngresosId = %s;"""
                cursor.execute(sql_update, (data['fecha'], data['concepto'], data['monto'], data['metodo_ingreso'], data['cuenta_ingreso'], data['descripcion'], data['UserId'], IngresosId))
                connection.commit()

        return jsonify({'message': 'Ingreso actualizado exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Método DELETE: Eliminar un ingreso por ID

def delete_insert_of_user(IngresosId):
    try:
        connection = conection_mysql.conectar()
        if connection is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

        with connection:
            with connection.cursor() as cursor:
                # Verificar si el ingreso existe
                sql_check = "SELECT IngresosId FROM ingresos WHERE IngresosId = %s;"
                cursor.execute(sql_check, (IngresosId,))
                result = cursor.fetchone()

                if not result:
                    return jsonify({'error': 'El ingreso con el ID proporcionado no existe'}), 404

                # Si existe, eliminarlo
                sql_delete = "DELETE FROM ingresos WHERE IngresosId = %s;"
                cursor.execute(sql_delete, (IngresosId,))
                connection.commit()

        return jsonify({'message': 'Ingreso eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ejecutar la API
if __name__ == '__main__':
    app.run(debug=True)