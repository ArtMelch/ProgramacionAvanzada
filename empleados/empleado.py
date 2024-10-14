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
    horario: datetime
     
    
    def __init__(self, id: str,nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_ingreso: datetime,rfc: str, curp: str, salario: float, horario: datetime):
        
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.rfc = rfc
        self.curp = curp
        self.salario = salario
<<<<<<< HEAD
        self.horario = horario
=======
        self.horario = horario
        self.rol = rol
        
    def mostrar_info_empl(self):
        nombre_completo = f"{self.nombre}{self.apellidos}"
        info = f"ID: {self.id} \nNombre completo: {nombre_completo} \nCURP: {self.curp} \nFecha de nacimiento: {self.fecha_nacimiento} \nRFC: {self.rfc} \nSalario: {self.salario} \nHorario: {self.horario} \nFecha de ingreso: {self.fecha_ingreso} \nRol: {self.rol.value}"
        return info
>>>>>>> a11872fe5db6df45e64c989bf0df10404f018f8c
