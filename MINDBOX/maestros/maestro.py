class Maestro:
    
    numero_control : int
    nombre : str
    apellido : str
    rfc : int
    sueldo : float
    
    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float):
        self.numero_control = "29232004"
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo