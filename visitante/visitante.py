from datetime import datetime

class Visitante:
    id_usuario: str
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    numero_visitas: int
    curp: str 
    fecha_registro: datetime
    
    def __init__(self, id_usuario:str,nombre: str, apellidos: str, fecha_nacimiento: str, numero_visitas: int, curp: str, fecha_registro: datetime):
        self.id_usuario= id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.numero_visitas = numero_visitas
        self.fecha_registro = fecha_registro
        