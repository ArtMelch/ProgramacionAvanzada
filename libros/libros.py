from datetime import date


class Libro:
    titulo : str
    autor : str
    editorial : str
    ano_publicacion : date
    precio : float
    
    def __init__(self, titulo:str, autor:str, editorial:str, ano_publicacion:date, precio:float):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_publicacion = ano_publicacion
        self.precio = precio