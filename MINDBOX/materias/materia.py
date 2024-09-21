class Materia:
    id : str 
    nombre : str
    descripcion : str
    semestre : int
    creditos: int
    
    def __init__(self, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos