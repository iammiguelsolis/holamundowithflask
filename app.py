from flask import Flask, jsonify

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
  
if __name__ == '__main__':
    app.run(debug=True, port=5000)