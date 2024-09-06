from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Usuarios para autenticación básica
users = {
    "admin": "password123"  
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Almacén temporal en memoria para los artículos
items = {}

@app.route('/')
def index():
    return "Bienvenido a la API de Inventario"

@app.route('/items', methods=['GET'])
@auth.login_required
def get_items():
    return jsonify(items)

@app.route('/item/<int:item_id>', methods=['POST'])
@auth.login_required
def create_item(item_id):
    if item_id in items:
        return jsonify({'message': 'Item ya existe'}), 400
    data = request.get_json()
    items[item_id] = data
    return jsonify({'message': 'Item creado'}), 201

@app.route('/item/<int:item_id>', methods=['GET'])
@auth.login_required
def get_item(item_id):
    item = items.get(item_id)
    if item is None:
        return jsonify({'message': 'Item no encontrado'}), 404
    return jsonify(item)

@app.route('/item/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_item(item_id):
    item = items.get(item_id)
    if item is None:
        return jsonify({'message': 'Item no encontrado'}), 404
    data = request.get_json()
    items[item_id] = data
    return jsonify({'message': 'Item actualizado'})

@app.route('/item/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_item(item_id):
    if item_id not in items:
        return jsonify({'message': 'Item no encontrado'}), 404
    del items[item_id]
    return jsonify({'message': 'Item eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
