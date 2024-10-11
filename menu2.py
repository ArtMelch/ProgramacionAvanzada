from empleados.utils.roles import Rol
from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from datetime import datetime

class Menu:
    zoo = Zoologico()
    
    def login(self):
        intentos = 0
        
        while intentos < 5:
            print("\n------BIENVENIDO AL SISTEMA DEL ZOOLÓGICO------\n")
            print("Inicia sesión para continuar: ")
            
            username = input("Ingresa el nombre de usuario: ")
            contrasena = input("Ingresa la contraseña: ")
            
            usuario = self.zoo.validad_inicio_sesion(username=username, contrasena=contrasena)
            
            if usuario is None:
                intentos = self.mostrar_intentos_sesion_fallido(intentos_usuario=intentos)
            
            else: 
                self.mostrar_menu()
                intentos = 0
        
        print("\n máximos intentos permitidos")
        
    def mostrar_intentos_sesion_fallidos(self, intentos_usuario):
        print("\nUsuario o contraseña incorrectos. Intente de nuevo\n")
        return intentos_usuario + 1
    
    def mostrar_menu(self):
        print("_______ M E N Ú ________")
        while True:
            menu = """
                1. Hacer registro
                2. Modificar
                3. Asignar mantenimientos
                4. Eliminar
                5. Consultar
            """
            print(menu)
            
            opcion = int(input("Ingresa una opción para continuar: "))
            
            if opcion == 1:
                print("\n*Seleccionaste hacer un registro*")
                
                menu_registro = """
                1. Registrar empleado
                2. Registrar animal
                3. Registrar visitantes
                4. Registrar visita
            """
                print(menu_registro)
            
                opcion_registro = int(input("Ingresa una opción para continuar: "))
                
                if opcion_registro == 1:
                    pass
                
                if opcion_registro == 2:
                    pass
                
                if opcion_registro == 3:
                    pass
                
                if opcion_registro == 4:
                    pass
                
            
            if opcion == 2:
                pass
            
            if opcion == 3:
                pass
            
            if opcion == 4:
                pass
            
            if opcion == 5:
                pass
            