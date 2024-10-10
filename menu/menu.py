from zoologico.zoologico import Zoologico


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
                1.
                2.
                3.
                4.
                5.
                6.
                7. Salir
            """
            print(menu)
            opcion = int(input("Escoge una acción: "))
            if opcion == 1:
                pass
            
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