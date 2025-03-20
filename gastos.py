from flask import Flask, request, jsonify
from conection_mysql import conectar

app = Flask(__name__)

db = conectar()  
cursor = db.cursor() 

@app.route('/')
def index():
    cursor.execute("SELECT GastosId, fecha, concepto, monto, metodo_pago, Cuenta_retiro, descripcion FROM gastos")
    gastos = cursor.fetchall()

    if not gastos:
        return jsonify({"message": "No hay gastos registrados"}), 404

    gastos_list = []
    for g in gastos:
        gastos_list.append({
            "GastosId": g["GastosId"],
            "fecha": str(g["fecha"]),
            "concepto": g["concepto"],
            "monto": g["monto"],
            "metodo_pago": g["metodo_pago"],
            "Cuenta_retiro": g["Cuenta_retiro"],
            "descripcion": g["descripcion"]
        })

    return jsonify(gastos_list)


@app.route("/add", methods=["POST"])
def add_gasto():
    try:
        data = request.get_json()
        cursor.execute(
            "INSERT INTO gastos (fecha, concepto, monto, metodo_pago, Cuenta_retiro, descripcion) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                data["fecha"],
                data["concepto"],
                data["monto"],
                data["metodo_pago"],
                data["Cuenta_retiro"],
                data["descripcion"],
            ),
        )
        db.commit()
        return jsonify({"message": "Gasto agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_gasto(id):
    cursor.execute("DELETE FROM gastos WHERE GastosId = %s", (id,))
    db.commit()
    return jsonify({"message": "Gasto eliminado correctamente"})


@app.route("/update/<int:id>", methods=["PUT"])
def update_gasto(id):
    try:
        data = request.get_json()
        cursor.execute(
            "UPDATE gastos SET fecha=%s, concepto=%s, monto=%s, metodo_pago=%s, Cuenta_retiro=%s, descripcion=%s WHERE GastosId=%s",
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
        db.commit()
        return jsonify({"message": "Gasto actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/gasto/<int:id>", methods=["GET"])
def get_gasto(id):
    cursor.execute("SELECT * FROM gastos WHERE GastosId = %s", (id,))
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


if __name__ == "__main__":
    app.run(debug=True)
