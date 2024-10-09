class Materia:
    id : str 
    nombre : str
    descripcion : str
    semestre : int
    creditos: int
    
    def __init__(self, id, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        
    def mostrar_info_materia(self):
        info = f"ID: {self.id} \nNombre: {self.nombre} \nDescripción: {self.descripcion}, \nSemestre: {self.semestre}, \nCreditos: {self.creditos}"
        return info