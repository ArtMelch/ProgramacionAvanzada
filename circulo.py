class Circulo:
    radio = 0
    
    #Método constructor
    def __init__(self, radio):
        self.radio = radio
        print("Radios: ", self.radio)
    
    def calcular_area(self):
        self.area = round(pow(self.radio, 2) * 3.1416, 3)
        print("Area: ", self.area)
    
    def calcular_perimetro(self):
        self.perimetro = round(2 * 3.1416 * self.radio, 3)
        print("Perimetro: ", self.perimetro)