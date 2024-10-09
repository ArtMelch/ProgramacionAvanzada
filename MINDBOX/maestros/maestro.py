from usuario.usuario import Usuario
from usuario.utils.roles import Rol


class Maestro(Usuario):
    rfc : int
    sueldo : float
    
    def __init__(self, numero_control:str, nombre: str, apellido: str, ano_nacimiento:int ,rfc: str, sueldo: float, contrasena: str):
        super().__init__(numero_control = numero_control, nombre= nombre, apellido=apellido,contrasena=contrasena, rol = Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        self.ano_nacimiento = ano_nacimiento
        
    def mostrar_info_mtr(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control} \nNombre completo: {nombre_completo} \nAño de nacimiento: {self.ano_nacimiento}\nRFC: {self.rfc} \nSueldo: {self.sueldo}"
        return info