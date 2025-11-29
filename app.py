from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios_db = [
    {"id": 1, "nombre": "Miguel", "rol": "Admin"},
    {"id": 2, "nombre": "Ana", "rol": "Cliente"},
    {"id": 3, "nombre": "Carlos", "rol": "Vendedor"}
]

@app.route('/')
def home():
    return "Servidor funcionando. Ve a /usuarios para ver la magia."
 
@app.route('/usuarios') 
def get_usuarios():
    return jsonify(usuarios_db)

@app.route('/usuarios/<int:id>')
def usuario_por_id(id):

    usuario = None
    
    for u in usuarios_db:
        if u['id'] == id:
            usuario = u
            break
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
      
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.get_json()
    
    if not nuevo_usuario.get('nombre') or not nuevo_usuario.get('rol'):
        return jsonify({"mensaje": "Faltan datos obligatorios"}), 400

    nuevo_usuario['id'] = len(usuarios_db) + 1
    usuarios_db.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201
  
if __name__ == '__main__':
    app.run(debug=True, port=5000)