from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    anos_antig: int
    
    def __init__(self, numero_control:str, nombre: str, apellido: str, contrasena: str, sueldo: float, rfc: str, anos_antig: int):
            super().__init__(numero_control = numero_control, nombre= nombre, apellido=apellido,contrasena=contrasena, rol = Rol.COORDINADOR)
            self.rfc = rfc
            self.sueldo = sueldo
            self.anos_antig = anos_antig
            
    def mostrar_info_coor(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control} \nNombre completo: {nombre_completo} \nRFC: {self.rfc} \nSueldo: {self.sueldo} \nAños de antigüedad: {self.anos_antig}"
        return info