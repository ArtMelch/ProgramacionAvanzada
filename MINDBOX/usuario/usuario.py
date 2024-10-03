from .utils.roles import Rol

class Usuario:
    numero_control: str
    nombre: str
    apellido: str
    contrasena: str
    rol: Rol
    
    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasena: str, rol: Rol):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        self.rol = rol