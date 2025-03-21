import conection_mysql
from flask import Flask, jsonify, request


app = Flask(__name__)

#OBTENER TODOS LOS USUARIOS
def get_all_users():
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

 #OBTENER UN SOLO USUARIO POR NUMERO DE CEDULA

def get_one_user(Cedula):
    try:
        connection = conection_mysql.conectar() #Conecta a la base de datos
        if connection is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500   
        
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT Nombre, Cedula, Telefono, Saldo_disponible_inicial FROM usuarios WHERE Cedula = %s'
                cursor.execute(sql, (Cedula,))
                result = cursor.fetchone()
                if result:
                    return jsonify({'data': result}), 200
                else:
                    return jsonify({'message': 'Usuario no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


#CREAR UN NUEVO USUARIO
def create_user():
    try:
       
        data = request.get_json()
        if not data or 'Nombre' not in data or 'Cedula' not in data  or 'Telefono' not in data  or 'Saldo_disponible_inicial' not in data :
            return jsonify({'error': 'Datos invalidos'}), 400
        connection = conection_mysql.conectar() #Conecta a la base de datos

        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO usuarios (Nombre, Edad, Cedula, Telefono, Saldo_disponible_inicial) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (data['Nombre'], data['Edad'], data['Cedula'], data['Telefono'], data['Saldo_disponible_inicial']))
            connection.commit()
        return jsonify({'message': 'Creacion Exitosa'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
 #ACTUALIZAR UN USUARIO POR EL NUMERO DE CEDULA   
def update_user(Cedula):
    try:
        data = request.get_json()
        if not data or 'Nombre' not in data or 'Cedula' not in data or 'Telefono' not in data or 'Saldo_disponible_inicial' not in data:
            return jsonify({'error': 'Datos invalidos'}), 400

        connection = conection_mysql.conectar() #Conecta a la base de datos
        with connection:
            with connection.cursor() as cursor:
                sql = 'UPDATE usuarios SET Nombre = %s, Cedula = %s, Telefono = %s, Saldo_disponible_inicial = %s WHERE Cedula = %s'
                cursor.execute(sql, (data['Nombre'], data['Cedula'], data['Telefono'], data['Saldo_disponible_inicial'], Cedula))
                connection.commit()
                if cursor.rowcount > 0:
                    return jsonify({'message': 'Los datos del usuario han sido actualizados'}), 200
                else:
                    return jsonify({'message': 'Usuario no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#ELIMINAR UN USUARIO POR EL NUMERO DE CEDULA  
def delete_user(Cedula):
    try:
        connection = conection_mysql.conectar()
        with connection:
            with connection.cursor() as cursor:
                # Eliminar registros relacionados en dashboard, ingresos, y gastos, y el usuario.
                sql_dashboard = 'DELETE FROM dashboard WHERE UsuarioId = (SELECT UsuarioId FROM usuarios WHERE Cedula = %s);'
                sql_ingresos = 'DELETE FROM ingresos WHERE UserId = (SELECT UsuarioId FROM usuarios WHERE Cedula = %s);'
                sql_gastos = 'DELETE FROM gastos WHERE UserId = (SELECT UsuarioId FROM usuarios WHERE Cedula = %s);'
                sql_usuarios = 'DELETE FROM usuarios WHERE Cedula = %s;'

                cursor.execute(sql_dashboard, (Cedula,))
                cursor.execute(sql_ingresos, (Cedula,))
                cursor.execute(sql_gastos, (Cedula,))
                cursor.execute(sql_usuarios, (Cedula,))

                connection.commit()
                if cursor.rowcount > 0:
                    return jsonify({'message': 'Usuario eliminado con exito'}), 200
                else:
                    return jsonify({'message': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)