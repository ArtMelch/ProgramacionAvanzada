from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint


class Semestre:
    id: str
    numero: int
    id_carrera: str
    materias: List[Materia]
    grupos: List[Grupo]
    
    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        
    def generar_id(self, numero_semestre) -> str:
        return f"{numero_semestre}-{randint(0, 100000)}-{randint(0, 100000)}"