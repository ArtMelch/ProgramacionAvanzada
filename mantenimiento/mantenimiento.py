from empleados.utils.roles import Rol
from empleados.empleado import Empleado
from datetime import datetime

class Mantenimiento(Empleado):
    pass

    def __init__(self, 
                 id: str,nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_ingreso: datetime,
                 rfc: str, curp: str, salario: float, horario: datetime):
        super().__init__(id=id,
                         nombre=nombre,
                         apellidos=apellidos,
                         fecha_nacimiento=fecha_nacimiento,
                         fecha_ingreso=fecha_ingreso,
                         rfc=rfc,
                         curp=curp,
                         salario=salario,
                         horario=horario,
                         rol=Rol.MANTENIMIENTO)
        
    def cuidado_animales(self):
        pass