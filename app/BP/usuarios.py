from flask import Blueprint, jsonify, request

from app.service.usuario_service import UsuarioService

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = UsuarioService.obtener_usuarios()
    return jsonify(usuarios), 200
  
@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = UsuarioService.obtener_usuario_por_id(id)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"mensaje": "Usuario no encontrado"}), 404
  
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    rol = data.get('rol')
    if not nombre or not rol:
        return jsonify({"mensaje": "Faltan datos obligatorios"}), 400
    nuevo_usuario = UsuarioService.crear_usuario(nombre, rol)
    return jsonify(nuevo_usuario), 201