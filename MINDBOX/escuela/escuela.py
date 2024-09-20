from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_grupos: List[Grupo] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
    
    def generar_numero_control_est(self):
        # L - 2024 - 09 - longitud lista estudiantes + 1 + random(0, 10000)
        ano = datetime.now().year
        mes = datetime.now().month
        aleatorio = randint(0,10000)
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def generar_numero_control_mtro(self, nombre, rfc, ano_nacimiento):
        # M - año - dia - random(500, 5000) - primeras 2 letras de su nombre - últimas 2 letras de su rfc - longitud lista maestros + 1
        ano_nacimiento = ano_nacimiento
        dia = datetime.now().day
        aleatorio = randint(500,5000)
        letras_nombre = nombre[:2]
        letras_nombre = letras_nombre.upper()
        letras_rfc = rfc[-2:]
        letras_rfc = letras_rfc.upper()
        longitud_mas_uno = len(self.lista_maestros) + 1
        numero_control = f"M{ano_nacimiento}{dia}{aleatorio}{letras_nombre}{letras_rfc}{longitud_mas_uno}"
        return numero_control
        