from usuarios.utils.rol import Rol

class Usuarios:
    nombre : str
    apellido : str
    usuario : str
    contrasena : str
    rol : Rol
    
    def __init__(self, nombre:str, apellido:str, usuario:str, contrasena:str, rol=Rol):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol
        