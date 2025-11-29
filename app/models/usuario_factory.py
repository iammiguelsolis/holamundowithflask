from app.models.usuario_model import Admin, Cliente, Usuario

class UsuarioFactory:
    @staticmethod
    def crear_usuario(id, nombre, rol):
        if rol == "Admin":
            return Admin(id, nombre, rol)
        elif rol == "Cliente":
            return Cliente(id, nombre, rol)
        else:
            return Usuario(id, nombre, rol)