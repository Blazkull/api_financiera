
from flask import Flask, jsonify
import usuarios, ingresos, dashboard, gastos

app = Flask(__name__)



#RUTAS DE USUARIOS
#RUTAS DE USUARIOS
@app.route('/api/users', methods=['GET'])
def get_all_users():
     return usuarios.get_all_users()

@app.route('/api/user/<int:Cedula>', methods=['GET'])
def get_one_user(Cedula):
     return usuarios.get_one_user(Cedula)

@app.route('/api/create/user', methods=['POST'])
def create_user():
     return usuarios.create_user()


@app.route('/api/update/users/<int:Cedula>', methods=['PUT'])
def update_user(Cedula):
     return usuarios.update_user(Cedula)

@app.route('/api/delete/user/<int:Cedula>', methods=['DELETE'])
def delete_user(Cedula):
     return usuarios.delete_user(Cedula)

#RUTAS DE DASHBOARD
@app.route('/api/users/dashboard', methods=['GET'])
def get_all_data_users():
     return dashboard.get_all_data_users()

@app.route('/api/user/dashboard/<int:cedula>', methods=['GET'])
def get_one_user_dashboard(Cedula):
     return dashboard.get_one_user_dashboard(Cedula)

  
#RUTAS DE INGRESOS
@app.route('/api/ingresos', methods=['GET'])
def get_all_ingresos():
     return ingresos.get_all_ingresos()

@app.route('/api/create/ingresos', methods=['POST'])
def crete_insert():
     return ingresos.crete_insert()

@app.route('/api/update/ingresos/<int:ingreso_id>', methods=['PUT'])
def update_insert__of_user(IngresosId):
     return ingresos.update_insert__of_user(IngresosId)

@app.route('/api/delete/ingresos/<int:ingreso_id>', methods=['DELETE'])
def delete_insert_of_user(IngresosId):
     return ingresos.delete_insert_of_user(IngresosId)





#RUTAS DE GASTOS
@app.route('/api/gastos', methods=['GET'])
def get_gasto():
    return gastos.get_gasto()

@app.route('/api/create/gastos', methods=['POST'])
def add_gasto():
    return gastos.add_gasto()

@app.route('/api/update/gastos/<int:GastosId>', methods=['PUT'])
def update_gasto(GastosId):
    return gastos.update_gasto(GastosId)

@app.route('/api/delete/gastos/<int:GastosId>', methods=['DELETE'])
def delete_gasto(GastosId):
    return gastos.delete_gasto(GastosId)

@app.route('/api/gastos/cedula/<int:cedula>', methods=['GET'])
def get_gastos_by_cedula(Cedula):
    return gastos.get_gastos_by_cedula(Cedula)

@app.route("/api/delete/gastos/cedula/<int:cedula>/gasto/<int:gasto_id>", methods=["DELETE"])
def delete_specific_gasto_by_cedula(Cedula, GastoId):
    return gastos.delete_specific_gasto_by_cedula(Cedula, GastoId)



if __name__ == '__main__':
    app.run(debug=True)


