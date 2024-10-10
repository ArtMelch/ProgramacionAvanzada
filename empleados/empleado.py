from datetime import datetime
from empleados.utils.roles import Rol


class Empleado:
    id = str
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    fecha_ingreso: datetime
    rfc: str
    curp: str
    salario: float
    horario: datetime
    rol: Rol 
    
    def __init__(self, 
                 nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_ingreso: datetime,
                 rfc: str, curp: str, salario: float, horario: datetime, rol: Rol):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.rfc = rfc
        self.salario = curp
        self.salario = salario
        self.horario = horario
        self.rol = rol