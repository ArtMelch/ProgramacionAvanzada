from datetime import datetime
from .utils.roles import Rol

class Usuario:
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    rol: Rol
    
    def __init__(self, nombre: str, apellidos: str, fecha_nacimiento:datetime, rol:Rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.rol = rol 
        