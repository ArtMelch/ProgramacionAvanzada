from datetime import datetime
from empleados.utils.roles import Tipo_Animal
from empleados.utils.roles import Alimentacion

class Animal:
    id: str
    tipo_animal: Tipo_Animal       #consultar (no str) CAMBIADO
    fecha_nacimiento: datetime
    fecha_llegada_zoo: datetime
    peso: float
    enfermedades: str
    frecuencia_alimentacion: str
    tipo_alimentacion: Alimentacion      #consultar (no str) CAMBIADO
    vacunas: bool
    #cambiar tipo de dato en tipo_animal y tipo_alimentación dentro de constructor
    def __init__(self,id: str,tipo_animal: Tipo_Animal,fecha_nacimiento: datetime,fecha_llegada_zoo: datetime,peso: float,enfermedades: str,frecuencia_alimentacion: str,tipo_alimentacion: Alimentacion,vacunas: bool):
        self.id = id
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_llegada_zoo= fecha_llegada_zoo
        self.peso = peso
        self.enfermedades = enfermedades
        self.frecuencia_alimentacion= frecuencia_alimentacion
        self.tipo_alimentacion= tipo_alimentacion
        self.vacunas= vacunas
    
    def mostar_info_animal(self):
        info = f"ID: {self.id} \nTipo de animal: {self.tipo_animal.value} \nFecha de nacimiento: {self.fecha_nacimiento} \nFecha de llegada: {self.fecha_llegada_zoo} \nPeso: {self.peso} \nTipo de alimentacion: {self.tipo_alimentacion.value} \nFrecuencia de alimentación: {self.frecuencia_alimentacion} \nEnfermedades: {self.enfermedades} \nVacunas: {self.vacunas}"
        return info
