from typing import List
from datetime import datetime
from random import randint
from empleados.empleado import Empleado
from visitante.visitante import Visitante
from animal.animal import Animal
from visitas.visitas import Visita
from empleados.utils.roles import Rol
from director.director import Director
from guia.guia import Guia #! ELIMINAR ANTES DE ENTREGAR
from visitante.visitante import Visitante #! ELIMINAR ANTES DE ENTREGAR
from visitas.visitas import Visita #! ELIMINAR ANTES DE ENTREGAR


class Zoologico:
    lista_empleados: List [Empleado] = []
    lista_guia : List [Empleado] = []
    lista_veterinario : List [Empleado] = []
    lista_mantenimiento : List [Empleado] = []
    lista_administrativo : List [Empleado] = []
    lista_visitantes: List [Visitante] = []
    lista_animales: List [Animal] = []
    lista_visitas: List [Visita] = []
    
    
    def __init__(self):
        director = Director(id="12345", nombre="Berta", apellidos= "Valencia", fecha_nacimiento= "12/05/10", fecha_ingreso= "03/06/24", rfc= "MRG09I09", curp= "BEMNL98987", salario= 10000, horario= "9-16", contrasena="321")
        self.lista_empleados.append(director)        
    
    
    #! REGISTRAR
    
    def registrar_empleado(self, empleado: Empleado, id: str):
        self.lista_empleados.append(empleado)
        letras_id = id[:2]
        if letras_id == "GI":
            self.lista_guia.append(empleado)
        
        elif letras_id == "VE":
            self.lista_veterinario.append(empleado)
            
        elif letras_id == "MA":
            self.lista_mantenimiento.append(empleado)
        
        elif letras_id == "AD":
            self.lista_administrativo.append(empleado)

    
    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        
    def registrar_visita(self, visita: Visita):
        precio_adulto = 100
        precio_niño = 50
        for visitante in visita.visitantes:
            visitante.numero_visitas += 1
            if visitante.numero_visitas % 5 == 0:
                print(f"Descuento del 20% para{visitante.nombre}")
                precio_final = precio_adulto*.8 if visitante.es_adulto() else precio_niño *.8
            else:
                precio_final = precio_adulto if visitante.es_adulto() else precio_niño
            print(f"visitante: {visitante.nombre}, precio boleto: ${precio_final}")
        self.lista_visitas.append(visita)
        print(f"visita registrada con ID: {visita.id}")
        
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
            rol=Rol.GUIA
            id = f"GI{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            
            return id, rol
        
        elif opcion == 2:
            rol=Rol.VETERINARIO
            id = f"VE{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id, rol
        
        elif opcion == 3:
            rol=Rol.MANTENIMIENTO
            id = f"MA{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id, rol
        
        elif opcion == 4:
            rol=Rol.ADMINISTRATIVO
            id = f"AD{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id, rol
    
    def generar_id_animal(self, tipo_animal, ano_llegada, ano_nacimiento):
        # Primeras dos letras del tipo de animal-dia de ingreso-año ingreso-año-nacimiento-numero de ingreso más 1
        dos_letras = tipo_animal.value[:2].upper()
        longitud_mas_uno = len(self.lista_animales) + 1
        
        id = f"{dos_letras}-{ano_llegada}{ano_nacimiento}{longitud_mas_uno}"
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
    
    #! ELIMINAR
    
    def eliminar_empleado(self, id:str):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                self.lista_empleados.remove(empleado)
                id_eliminar = id[:2]
                
                if id_eliminar == "VE":
                    self.lista_veterinario.remove(empleado)
                    
                elif id_eliminar == "MA":
                    self.lista_mantenimiento.remove(empleado)
                
                elif id_eliminar == "AD":
                    self.lista_administrativo.remove(empleado)
                
                elif id_eliminar == "GI":
                    self.lista_guia.remove(empleado)
                
                else:
                    print("ANONIMUS FATAL ERROR ")
                    
                print("Empleado eliminado")
                return
        print(f"\n\tNo se encontró al empleado con el ID: {id}")
    
    def eliminar_animal(self, id: str):
        for animal in self.lista_animales:
            if animal.id == id:
                self.lista_animales.remove(animal)
                print("\n\tAnimal extinguido")
                return
        print(f"\n\tNo hay animal con el id: {id}")
    
    def eliminar_visita(self, id: str):
        for visita in self.lista_visitas:
            if visita.id == id:
                self.lista_visitas.remove(visita)
                print("\n\tSe eliminó la visita")
                return
        print(f"\n\tNo se encontro la visita con el id: {id}")
        
    #! LISTAR
    
    def listar_empleados(self):
        print("\n--------------EMPLEADOS-------------\n")
        for empleado in self.lista_empleados:
            print(empleado.mostrar_info_empl())
            
    def listar_veterinarios(self):
        print("\n--------------VETERINARIOS-------------\n")
        for empleado in self.lista_veterinario:
            print(empleado.mostrar_info_empl())
            
    def listar_guias(self):
        print("\n--------------GUÍAS-------------\n")
        for empleado in self.lista_guia:
            print(empleado.mostrar_info_empl())
            
    def listar_mantenimiento(self):
        print("\n--------------MANTENIMIENTO-------------\n")
        for empleado in self.lista_mantenimiento:
            print(empleado.mostrar_info_empl())
            
    def listar_administrativos(self):
        print("\n--------------VETERINARIOS-------------\n")
        for empleado in self.lista_administrativo:
            print(empleado.mostrar_info_empl())
            
    def listar_animales(self):
        print("\n-------------ANIMALES---------------\n")
        for animal in self.lista_animales:
            print(animal.mostar_info_animal())
            
    def listar_visitas(self):
        print("\n-------------VISITAS-------------\n")
        for visita in self.lista_visitas:
            print(visita.mostrar_info_visitas())
    
    def listar_visitantes(self):
        print("\n----------VISITANTES-----------\n")
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
    
    #! VALIDAR INICIO DE SESIÓN
    
    def validar_inicio_sesion(self, id: str, contrasena: str):
        for director in self.lista_empleados:
            if director.id == id:
                if director.contrasena == contrasena:
                    return director
                
        return None