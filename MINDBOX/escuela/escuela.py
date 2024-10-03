from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carreras.carrera import Carrera
from semestres.semestre import Semestre
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_grupos: List[Grupo] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    
    
    #/ GENERAR ID'S
    def generar_numero_control_est(self):
        # L - 2024 - 09 - longitud lista estudiantes + 1 + random(0, 10000)
        ano = datetime.now().year
        mes = datetime.now().month
        aleatorio = randint(0, 10000)
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
    
    def generar_id_materia(self, nombre, semestre, creditos):
        nombre = nombre.upper()
        digitos_nombre = nombre[-2:]
        semestre = semestre
        cantidad_creditos = creditos
        
        id = f"MT{digitos_nombre}{semestre}{cantidad_creditos}{randint(1,1000)}"
        return id
    
    
    #/ REGISTRAR
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
        
    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
    
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
        
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id
        
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre = semestre)
                break
            
        self.lista_semestres.append(semestre)
    
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        
        for semestre in self.lista_semestres:
            if semestre.id == id_semestre:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        
        self.lista_grupos.append(grupo)
    
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
        print("\n\tEstudiante registrado con exíto")
    
    
    #/ LISTAR
    def listar_estudiantes(self):
        print("\n--------ESTUDIANTES----------\n")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_est())
            
    def listar_maestros(self):
        print("\n--------MAESTROS----------\n")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_mtr())
    
    def listar_materias(self):
        print("\n--------MATERIAS----------\n")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
    
    def listar_carreras(self):
        print("\n--------CARRERAS----------\n")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
            
    def listar_semestres(self):
        print("\n--------SEMESTRES---------\n")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestres())
    
    def listar_grupos(self):
        print("\n--------GRUPOS------------\n")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
    
    #/ ELIMINAR
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        print(f"\n\tNo se encontró el estudiante con el número de control: {numero_control}")
        
    
    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        print(f"\n\tNo se encontró el maestro con el número de control: {numero_control}")
    
    def eliminar_materia(self, id: str):
        for materia in self.lista_materias:
            if materia.id == id:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
        print(f"No se encontró la materia con el número de control: {id}")
        
    