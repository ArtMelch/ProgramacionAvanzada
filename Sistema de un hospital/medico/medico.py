import random

class Medico:
    id : int
    nombre : str
    ano_nacimiento : int
    rfc = str
    direccion = str
    
    def __init__(self, nombre : str, ano_nacimiento : int, rfc : str, direccion : str):
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