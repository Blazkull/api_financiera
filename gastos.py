from flask import Flask, request, jsonify
from conection_mysql import conectar

app = Flask(__name__)


@app.route("/api/gastos")
def get_gasto():
    try:
        with conectar() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT GastosId, fecha, concepto, monto, metodo_pago, Cuenta_retiro, descripcion FROM gastos"
                cursor.execute(sql)
                gastos = cursor.fetchall()

                if not gastos:
                    return jsonify({"message": "No hay gastos registrados"}), 404

                gastos_list = [
                    {
                        "GastosId": g["GastosId"],
                        "fecha": str(g["fecha"]),
                        "concepto": g["concepto"],
                        "monto": g["monto"],
                        "metodo_pago": g["metodo_pago"],
                        "Cuenta_retiro": g["Cuenta_retiro"],
                        "descripcion": g["descripcion"],
                    }
                    for g in gastos
                ]

                return jsonify(gastos_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/add", methods=["POST"])
def add_gasto():
    try:
        data = request.get_json()
        with conectar() as connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO gastos (fecha, concepto, monto, metodo_pago, Cuenta_retiro, descripcion) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(
                    sql,
                    (
                        data["fecha"],
                        data["concepto"],
                        data["monto"],
                        data["metodo_pago"],
                        data["Cuenta_retiro"],
                        data["descripcion"],
                    ),
                )
            connection.commit()
        return jsonify({"message": "Gasto agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/delete/<int:GastosId>", methods=["DELETE"])
def delete_gasto(GastosId):
    try:
        with conectar() as connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM gastos WHERE GastosId = %s"
                cursor.execute(sql, (id,))
            connection.commit()
        return jsonify({"message": "Gasto eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/update/<int:GastosId>", methods=["PUT"])
def update_gasto(GastosId):
    try:
        data = request.get_json()
        with conectar() as connection:
            with connection.cursor() as cursor:
                sql = """UPDATE gastos 
                         SET fecha=%s, concepto=%s, monto=%s, metodo_pago=%s, Cuenta_retiro=%s, descripcion=%s 
                         WHERE GastosId=%s"""
                cursor.execute(
                    sql,
                    (
                        data["fecha"],
                        data["concepto"],
                        data["monto"],
                        data["metodo_pago"],
                        data["Cuenta_retiro"],
                        data["descripcion"],
                        id,
                    ),
                )
            connection.commit()
        return jsonify({"message": "Gasto actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/gastos/cedula/<int:cedula>", methods=["GET"])
def get_gastos_by_cedula(cedula):
    try:
        with conectar() as connection:
            with connection.cursor() as cursor:
                sql = """
                SELECT g.GastosId, g.Fecha, g.Concepto, g.Monto, g.Metodo_pago, 
                       g.Cuenta_retiro, g.Descripcion, u.Cedula 
                FROM gastos g
                JOIN usuarios u ON g.UserId = u.UsuarioId
                WHERE u.Cedula = %s
                """
                cursor.execute(sql, (cedula,))
                gastos = cursor.fetchall()

                if not gastos:
                    return (
                        jsonify(
                            {"message": "No hay gastos registrados para esta cédula"}
                        ),
                        404,
                    )

                gastos_list = [
                    {
                        "GastosId": g["GastosId"],
                        "Fecha": str(g["Fecha"]),
                        "Concepto": g["Concepto"],
                        "Monto": g["Monto"],
                        "Metodo_pago": g["Metodo_pago"],
                        "Cuenta_retiro": g["Cuenta_retiro"],
                        "Descripcion": g["Descripcion"],
                        "Cedula": g["Cedula"],
                    }
                    for g in gastos
                ]

                return jsonify(gastos_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/gastos/cedula/<int:cedula>/gasto/<int:gasto_id>", methods=["DELETE"])
def delete_specific_gasto_by_cedula(cedula, gasto_id):
    try:
        with conectar() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT UsuarioId FROM usuarios WHERE Cedula = %s", (cedula,)
                )
                usuario = cursor.fetchone()

                if not usuario:
                    return (
                        jsonify({"message": "No existe un usuario con esta cédula"}),
                        404,
                    )

                usuario_id = usuario["UsuarioId"]
                cursor.execute(
                    "SELECT * FROM gastos WHERE GastosId = %s AND UserId = %s",
                    (gasto_id, usuario_id),
                )
                gasto = cursor.fetchone()

                if not gasto:
                    return (
                        jsonify(
                            {
                                "message": "No se encontró un gasto con ese ID para esta cédula"
                            }
                        ),
                        404,
                    )
                
                cursor.execute("DELETE FROM gastos WHERE GastosId = %s", (gasto_id,))
                connection.commit()

                return (
                    jsonify({"message": "El gasto ha sido eliminado exitosamente"}),
                    200,
                )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
