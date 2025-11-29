from models.usuario_model import Usuario

class UsuarioService:
  db_usuarios = [
    Usuario(1, "Miguel", "Admin"),
    Usuario(2, "Ana", "Cliente"),
    Usuario(3, "Carlos", "Vendedor")
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
    nuevo_id = len(UsuarioService.db_usuarios) + 1
    nuevo_usuario = Usuario(nuevo_id, nombre, rol)
    UsuarioService.db_usuarios.append(nuevo_usuario)
    return nuevo_usuario.to_json()