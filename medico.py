import random

class Medico:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    rfc = ""
    direccion = ""
    
    def __init__(self, nombre, ano_nacimiento, rfc, direccion):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion
        
    def mostrar_info_medico(self):
        print(f"\nNombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"RFC: {self.rfc}")
        print(f"Dirección: {self.direccion}")
    
    #Getters
    
    # @property
    # def id(self):
    #     return self.id
    
    # @property
    # def nombre(self):
    #     return self.nombre
    
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    
    # @property
    # def peso(self):
    #     return self.rfc
    
    # @property
    # def estatura(self):
    #     return self.estatura
    
    # @property
    # def direccion(self):
    #     return self.direccion