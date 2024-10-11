from datetime import datetime
from empleados.utils.roles import Rol

class Animal:
    id: str
    tipo_animal: Rol       #consultar (no str) CAMBIADO
    fecha_nacimiento: datetime
    fecha_llegada_zoo: datetime
    peso: float
    enfermedades: str
    frecuencia_alimentacion: str
    tipo_alimentacion: Rol      #consultar (no str) CAMBIADO
    vacunas: bool
    #cambiar tipo de dato en tipo_animal y tipo_alimentación dentro de constructor
    def _init_(self,
                 id: str,
                 tipo_animal: Rol,
                 fecha_nacimiento: datetime,
                 fecha_llegada_zoo: datetime,
                 peso: float,
                 enfermedades: str,
                 frecuencia_alimentacion: str,
                 tipo_alimentacion: Rol,
                 vacunas: bool):
        
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_llegada_zoo= fecha_llegada_zoo
        self.peso = peso
        self.enfermedades = enfermedades
        self.frecuencia_alimentacion= frecuencia_alimentacion
        self.tipo_alimentacion= tipo_alimentacion
        self.vacunas= vacunas