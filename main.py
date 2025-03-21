## aqui va todo el llamado a cada una de la funciones de los codigos


from flask import Flask,jsonify
import usuarios,ingresos,dashboard,gastos

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_all_users():
     return usuarios.get_all_users()

@app.route('/api/user/<int:Cedula>', methods=['GET'])
def get_one_user(Cedula):
     return usuarios.get_one_user(Cedula)

@app.route('/api/usuarios', methods=['POST'])
def create_user():
     return usuarios.create_user()


@app.route('/api/users/<int:Cedula>', methods=['PUT'])
def update_user(Cedula):
     return usuarios.update_user()

@app.route('/api/users/<int:Cedula>', methods=['DELETE'])
def delete_user(Cedula):
     return usuarios.delete_user

if __name__ == '__main__':
    app.run(debug=True)