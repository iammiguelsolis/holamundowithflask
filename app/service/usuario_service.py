from app.models.usuario_model import Usuario
from app.models.usuario_factory import UsuarioFactory
from app.utils.validaciones import es_texto_valido

class UsuarioService:
  db_usuarios = [
    UsuarioFactory.crear_usuario(1, "Alice", "Admin"),
    UsuarioFactory.crear_usuario(2, "Bob", "Cliente"),
    UsuarioFactory.crear_usuario(3, "Charlie", "Usuario"),
  ]
  
  @staticmethod
  def obtener_usuarios():
    return [usuario.to_json() for usuario in UsuarioService.db_usuarios]
  
  @staticmethod
  def obtener_usuario_por_id(id):
    for usuario in UsuarioService.db_usuarios:
      if usuario.id == id:
        return usuario.to_json()
    return None
  
  @staticmethod
  def crear_usuario(nombre, rol):
    if not es_texto_valido(nombre) or not es_texto_valido(rol):
      raise ValueError("Nombre y rol deben ser textos válidos")
    
    nuevo_id = max([usuario.id for usuario in UsuarioService.db_usuarios]) + 1
    nuevo_usuario = UsuarioFactory.crear_usuario(nuevo_id, nombre, rol)
    UsuarioService.db_usuarios.append(nuevo_usuario)
    return nuevo_usuario.to_json()