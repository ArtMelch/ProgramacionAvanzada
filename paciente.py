import random

class Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""
    
    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion
    
    def mostrar_info_paciente(self):
        print("\nId: ", self.id)
        print(f"Nombre: {self.nombre}") #Hace lo mismo que la linea 20. La "f" es de formateado
        print("Año de nacimiento:", self.ano_nacimiento)
        print("Peso:", self.peso)
        print("Estatura:", self.estatura)
        print("Dirección:", self.direccion)
        
    def mostrar_info_nino(self):
        print("\nId: ", self.id)
        print(f"Nombre: {self.nombre}") #Hace lo mismo que la linea 20. La "f" es de formateado
        print("Año de nacimiento:", self.ano_nacimiento)
        print("Peso:", self.peso)
        print("Estatura:", self.estatura)
        print("Dirección:", self.direccion)
        
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
    #     return self.peso
    
    # @property
    # def estatura(self):
    #     return self.estatura
    
    # @property
    # def direccion(self):
    #     return self.direccion