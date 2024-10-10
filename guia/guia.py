from empleados.empleado import Empleado
from empleados.utils.roles import Rol

class Guia(Empleado):
    rol:Rol
    
    def __init__(self,rol:Rol.GUIA):
        