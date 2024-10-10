from empleados.empleado import Usuario
from empleados.utils.roles import Rol
from datetime import datetime

class Visitante(Usuario):
    numero_visitas: int
    curp: str 
    fecha_registro: datetime
    
    def __init__(self, nombre: str, apellidos: str, fecha_nacimiento: str, numero_visitas: int, curp: str, fecha_registro: datetime):
        super().__init__(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, rol=Rol.VISITANTE)
        self.curp = curp
        self.numero_visitas = numero_visitas
        self.fecha_registro = fecha_registro
        