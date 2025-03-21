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
                cursor.execute(sql, (GastosId,))
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
                        ,
                    ),
                )
            connection.commit()
        return jsonify({"message": "Gasto actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/gasto/<int:Gastos>", methods=["GET"])
def get_gasto_id(GastosId):
    try:
        with conectar() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM gastos WHERE GastosId = %s"
                cursor.execute(sql, (GastosId,))
                gasto = cursor.fetchone()

                if gasto:
                    gasto_dict = {
                        "GastosId": gasto["GastosId"],
                        "fecha": str(gasto["fecha"]),
                        "concepto": gasto["concepto"],
                        "monto": gasto["monto"],
                        "metodo_pago": gasto["metodo_pago"],
                        "Cuenta_retiro": gasto["Cuenta_retiro"],
                        "descripcion": gasto["descripcion"],
                    }
                    return jsonify(gasto_dict)

                return jsonify({"error": "Gasto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
