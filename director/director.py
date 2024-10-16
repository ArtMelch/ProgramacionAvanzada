from empleados.empleado import Empleado
from empleados.utils.roles import Rol

class Director(Empleado):
    contrasena: str  
    
    def __init__(self, id: str,nombre: str, apellidos: str, fecha_nacimiento: str, fecha_ingreso: str, rfc: str, curp: str, salario: float, horario: str, contrasena: str):
        super().__init__(id=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_ingreso=fecha_ingreso, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=Rol.DIRECTOR)
        self.contrasena = contrasena
        
    def mostrar_info_empl(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"ID: {self.id} \nNombre completo: {nombre_completo} \nCURP: {self.curp} \nFecha de nacimiento: {self.fecha_nacimiento} \nRFC: {self.rfc} \nSalario: {self.salario} \nHorario: {self.horario} \nFecha de ingreso: {self.fecha_ingreso} \nRol: {self.rol.value}\n"
        return info