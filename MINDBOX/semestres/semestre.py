from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint


class Semestre:
    id: str
    numero: int
    id_carrera: str
    numero_grupos : int = 0
    materias: List[Materia] = []
    grupos: List[Grupo] = []
    
    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero = numero
        
    def generar_id(self, numero_semestre) -> str:
        return f"{numero_semestre}-{randint(0, 100000)}-{randint(0, 100000)}"
    
    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.numero_grupos += 1
        self.grupos.append(grupo)
        
    def mostrar_info_semestres(self):
        info = f"ID: {self.id} \nNúmero: {self.numero} \nID de la carrera: {self.id_carrera}"
        return info