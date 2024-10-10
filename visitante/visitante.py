from usuario.usuario import Usuario
from usuario.utils.roles import Rol
from datetime import datetime

class Visitante:
    numero_visitas: int
    curp: str 
    fecha_registro: datetime
    
    def __init__(self, nombre: str, numero_visitas: int, curp: str, fecha_registro: datetime):
        super().__init__(numero_visitas = numero_visitas, nombre = nombre)
        pass