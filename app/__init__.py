from flask import Flask, jsonify
from .BP.usuarios import usuarios_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(usuarios_bp)
    
    @app.route('/')
    def home():
        return jsonify({"mensaje": "¡Bienvenido a la API de Usuarios!"})
    
    return app