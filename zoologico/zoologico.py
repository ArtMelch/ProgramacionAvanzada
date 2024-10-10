from typing import List
from empleados.empleado import Empleado
from visitante.visitante import Visitante
from animal.animal import Animal
from visitas.visitas import Visita


class Zoologico:
    lista_empleados: List [Empleado] = []
    lista_visitantes: List [Visitante] = []
    lista_animales: List [Animal] = []
    lista_visitas: List [Visita] = []
    
    def __init__(self):
        pass
    
    
    #! REGISTRAR
    
    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
    
    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        
    def registrar_visita(self, visita: Visita):
        self.lista_visitas.append(visita)
        
    def registrar_animal(self, animal: Animal):
        self.lista_animales.append(animal)