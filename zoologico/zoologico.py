from typing import List
from datetime import datetime
from random import randint
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
        
    #! GENERAR ID'S
    
    def generar_id_empleados(self, nombre, ano_nacimiento):
        ano_nacimiento = ano_nacimiento
        dia = datetime.now().day
        aleatorio = randint(100,1000)
        letras_nombre = nombre[:2]
        letras_nombre = letras_nombre.upper()
        longitud_mas_uno = len(self.lista_empleados) +1
        
        menu = """
        EMPLEADOS
        
        1. Guía
        2. Veterinario
        3. Mantenimiento
        4. Administrador
    
        """  
        print(menu)
        opcion = int(input("Rol del empleado: "))
        
        if opcion == 1:
            id = f"GI{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id
        
        elif opcion == 2:
            id = f"VE{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id
        
        elif opcion == 3:
            id = f"MA{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id
        
        elif opcion == 4:
            id = f"AD{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id
    
    def generar_id_animal(self, tipo_animal, ano_llegada, ano_nacimiento):
        # Primeras dos letras del tipo de animal-dia de ingreso-año ingreso-año-nacimiento-numero de ingreso más 1
        tipo_animal = tipo_animal[:2]
        longitud_mas_uno = len(self.lista_animales) + 1
        
        id = f"{tipo_animal}-{ano_llegada}{ano_nacimiento}{longitud_mas_uno}"
        return id
    
    def generar_id_visitante(self, ano_nacimiento):
        longitud_mas_uno = len(self.lista_visitantes) +1
        numero_random = randint(10,100)
        
        id = f"VISITANTE{ano_nacimiento}{numero_random}{longitud_mas_uno}"
        return id
    
    def generar_id_visita(self):
        numero_random = randint(100,1000)
        longitud_mas_uno = len(self.lista_visitas) + 1
        
        id = f"VISITA{numero_random}{longitud_mas_uno}"
        return id