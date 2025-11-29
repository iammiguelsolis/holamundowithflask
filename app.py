from flask import Flask
from BP.usuarios import usuarios

app = Flask(__name__)

app.register_blueprint(usuarios)

@app.route('/')
def home():
    return "Bienvenido a la API de Usuarios"

if __name__ == '__main__':
    app.run(debug=True, port=5000)