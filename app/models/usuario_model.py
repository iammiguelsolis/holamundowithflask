class Usuario:
  def __init__(self, id, nombre, rol):
    self.id = id
    self.nombre = nombre
    self.rol = rol
    
  def get_permisos(self):
    return 'Basicos'
  
  def to_json(self):
    return {
      "id": self.id,
      "nombre": self.nombre,
      "rol": self.rol,
      "permisos": self.get_permisos()
    }

class Admin(Usuario):
  
  def __init__(self, id, nombre, rol):
    super().__init__(id, nombre, rol)
  
  def get_permisos(self):
    return 'Acceso completo'
  
class Cliente(Usuario):
  
  def __init__(self, id, nombre, rol):
    super().__init__(id, nombre, rol)
  
  def get_permisos(self):
    return 'Acceso limitado'