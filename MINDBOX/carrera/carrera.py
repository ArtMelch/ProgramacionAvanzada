from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestre.semestre import Semestre

class Carrera:
    matricula: str
    nombre: str
    numero_semestres: int
    semestres: List[Semestre]
    