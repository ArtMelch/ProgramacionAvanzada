from datetime import datetime
from empleados.utils.roles import Rol


class Empleado:
    id : str
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    fecha_ingreso: datetime
    rfc: str
    curp: str
    salario: float
    horario: str
    rol: Rol
     
    
    def __init__(self, id: str,nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_ingreso: datetime,rfc: str, curp: str, salario: float, horario: str, rol: Rol):
        
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.rfc = rfc
        self.curp = curp
        self.salario = salario
        self.horario = horario
        self.rol = rol
        
    def mostrar_info_empl(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"ID: {self.id} \nNombre completo: {nombre_completo} \nCURP: {self.curp} \nFecha de nacimiento: {self.fecha_nacimiento} \nRFC: {self.rfc} \nSalario: {self.salario} \nHorario: {self.horario} \nFecha de ingreso: {self.fecha_ingreso} \nRol: {self.rol.value}\n"
        return info
