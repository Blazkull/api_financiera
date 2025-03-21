from flask import Flask, jsonify
import usuarios, ingresos, dashboard, gastos

app = Flask(__name__)

# RUTAS DE GASTOS
@app.route('/api/gastos', methods=['GET'])
def get_gasto():
    return gastos.get_gasto()

@app.route('/api/create/gastos', methods=['POST'])
def add_gasto():
    return gastos.add_gasto()

@app.route('/api/update/gastos/<int:GastosId>', methods=['PUT'])
def update_gasto(GastosId):
    return gastos.update_gasto()

@app.route('/api/delete/gastos/<int:GastosId>', methods=['DELETE'])
def delete_gasto(GastosId):
    return gastos.delete_gasto()

@app.route('/api/gastos/cedula/<int:cedula>', methods=['GET'])
def get_gastos_by_cedula(cedula)
    return gastos.get_gastos_by_cedula(cedula)

@app.route("/api/delete/gastos/cedula/<int:cedula>/gasto/<int:gasto_id>", methods=["DELETE"])
def delete_specific_gasto_by_cedula(cedula, gasto_id):
    return gastos.delete_specific_gasto_by_cedula(cedula, gasto_id):

if __name__ == '__main__':
app.run(debug=True)