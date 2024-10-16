from datetime import datetime
from empleados.utils.roles import Rol

class Visitante:
    id_visitante: str
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    numero_visitas: int
    curp: str 
    fecha_registro: datetime
    rol: Rol
    
    def __init__(self, id_visitante:str, nombre: str, apellidos: str, fecha_nacimiento: str, curp: str, fecha_registro: datetime, numero_visitas: int): #!Creo que no va el rol
        self.id_visitante= id_visitante
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.numero_visitas = numero_visitas
        self.fecha_registro = fecha_registro
        self.rol = Rol.VISITANTE
        
        

    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"ID: {self.id_visitante} \nNombre: {nombre_completo} \nCURP: {self.curp} \nFecha de nacimiento: {self.fecha_nacimiento} \nFecha de registro: {self.fecha_registro} \nNúmero de visitas: {self.numero_visitas}\n"
        return info
    
    def es_adulto(self):
        hoy = datetime.now()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad >= 18
        