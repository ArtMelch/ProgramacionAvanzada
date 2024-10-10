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
        opcion = 0
        while opcion != 7:
            menu = """
                ZOOLÓGICO
                1. Registrar empleado
                2. Registrar animal
                3. Registrar visitante
                4. Registrar visita
                5.
                6.
                7. Salir
            """
            print(menu)
            opcion = int(input("Escoge una acción: "))
            if opcion == 1:
                print("\nSelecionaste: Registrar empleado\n")
                
                id = self.zoo.generar_id()
                print("ID: ", id)
                nombre = input("Nombre del empleado: ")
                apellidos = input("Apellidos: ")
                ano_ingreso = input("Año de ingreso: ")
                mes_ingreso = input("Mes de ingreso: ")
                dia_ingreso = input("Día de ingreso: ")
                salario = float(input("Ingresa el salario: "))
                rfc = input("Ingrese RFC: ")
                curp = input("Ingrese la CURP: ")
                horario = input("Ingrese el horario del empleado: ")
                ano_nacimiento = int(input("Año de nacimiento: "))
                mes_nacimiento = int(input("Mes de nacimiento: "))
                dia_nacimiento = int(input("Día de nacimiento: "))
                
                fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                fecha_ingreso = datetime(ano_ingreso, mes_ingreso, dia_ingreso)
                
                empleado = Empleado(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_ingreso=fecha_ingreso, rfc=rfc, curp=curp, salario=salario, horario=horario)
                self.zoo.registrar_empleado(empleado = empleado)
            
            elif opcion == 2:
                pass
            
            elif opcion == 3:
                pass
            
            elif opcion == 4:
                pass
            
            elif opcion == 5:
                pass
            
            elif opcion == 6:
                pass
            
            elif opcion == 7:
                break