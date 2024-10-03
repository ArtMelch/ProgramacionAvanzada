from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carreras.carrera import Carrera
from semestres.semestre import Semestre
from grupos.grupo import Grupo
from datetime import datetime


class Menu:
    escuela = Escuela()
    usuario_estudiante: str = "Juan123"
    contrasena_estudiante: str = "12345*"
    
    usuario_maestro: str = "mario123"
    contrasena_maestro: str = "54321*"
    
    
    def login(self):
        intentos = 0
        
        while intentos < 5:
            print("\n----BIENVENIDO----\n")
            print("Inicia sesión para continuar")
            
            nombre_usuario = input("\nIngresa tu nombre de usuario: ")
            contrasena_usuario = input("Ingresa tu contraseña: ")
            
            if nombre_usuario == self.usuario_estudiante:
                
                if contrasena_usuario == self.contrasena_estudiante:
                    self.mostrar_menu_estudiante()
                    intentos = 0
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario = intentos)
                    
            elif nombre_usuario == self.usuario_maestro:
                if contrasena_usuario == self.contrasena_maestro:
                    self.mostrar_menu_maestro()
                    intentos = 0
                    
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario = intentos)
                
            else:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario = intentos)
                
        print("\nMáximos intentos permitidos. Adios basura")
    
    
    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("\nUsuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1
    
    def mostrar_menu_estudiante(self):
        print("MENÚ DEL ESTUDIANTE")
        opcion = 0
        while opcion != 3:
            menu1 = """
                MINDBOX
                1. Ver horarios
                2. Ver grupos
                3. Ver materias
                4. Salir   
            """
            #! AGREGAR MÁS OPCIONES
            print(menu1)
            opcion = int(input("Ingresa una opción: "))
            
            if opcion == 3:
                break
            
            
    
    def mostrar_menu_maestro(self):
        print("MENÚ DEL MAESTRO")
        opcion = 0
        while opcion != 5:
            menu1 = """
                MINBOX
                1. Ver horarios
                2. Ver grupos
                3. Ver materias
                4. Ver alumnos
                5. Salir 
            """
            #! AGREGAR MÁS OPCIONES
            print(menu1)
            opcion = int(input("Ingresa una opción: "))
            
            if opcion == 5:
                break
    
    def mostrar_menu(self):
        menu1 = """
___________MINDBOXS__________

    1) Registrar estudiante
    2) Registrar maestro
    3) Registrar materia
    4) Registrar horario
    5) Registrar carrera
    6) Registrar semestre
    7) Registrar grupo
    
    8) Mostrar estudiantes
    9) Mostrar maestros
    10) Mostrar materias
    11) Mostrar carrera
    12) Mostrar semestres
    13) Mostrar grupos
    
    14) Eliminar estudiante
    15) Eliminar maestro
    16) Eliminar materia
    17) Salir

        """

        while True:
            print(menu1)
            opcion = input("Ingresa una opción para continuar: ")
            
            if opcion == "1":
                print("\nSeleccionaste: Registrar estudiante\n")
                
                numero_control = self.escuela.generar_numero_control_est()
                print("No.Control: ",numero_control)
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa el curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el día de nacimiento del estudiante: "))
                contrasena= (input("Ingresa la contraseña: "))
                
                fecha_nacimiento = datetime(ano, mes, dia)
                
                estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, contrasena=contrasena)
                self.escuela.registrar_estudiante(estudiante = estudiante)
                
            elif opcion == "2":
                print("\nSeleccionaste: Registrar maestro\n")
                nombre = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ")
                rfc = input("Ingresa el RFC del maestro: ")
                ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
                sueldo = float(input("Ingresa el sueldo del maestro: "))
                contrasena= (input("Ingresa la contraseña: "))
                
                numero_control = self.escuela.generar_numero_control_mtro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
                print("num control: ", numero_control)
                maestro = Maestro(nombre=nombre, apellido=apellido, rfc=rfc,ano_nacimiento=ano_nacimiento, sueldo=sueldo, contrasena=contrasena)
                self.escuela.registrar_maestro(maestro = maestro)
                
            elif opcion == "3":
                print("\nSeleccionaste: Registrar materia")
                nombre = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa la descripción de la materia: ")
                semestre = int(input("Ingresa el semestre de la materia: "))
                creditos = int(input("Ingresa el número de créditos del semestre: "))
                
                id = self.escuela.generar_id_materia(nombre, semestre, creditos)
                print(id)
                materia = Materia(id=id, nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
                self.escuela.registrar_materia(materia = materia)
            
            elif opcion == "4":
                pass
            
            elif opcion == "5":
                print("\nSeleccionaste: Registrar Carrera\n")
                nombre = input("Ingresa el nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera = carrera)
            
            elif opcion == "6":
                print("\nSeleccionaste: Registrar semestre\n")
                numero = int(input("Ingresa el numero del semestre: "))
                id_carrera = input("Ingresa el ID de la carrera: ")
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)
            
            elif opcion == "7":
                print("\nSeleccionaste: Registrar grupo\n")
                tipo = input("Ingresa el tipo de grupo (A/B): ")
                id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")
                grupo = Grupo(tipo = tipo, id_semestre = id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)
            
            elif opcion == "8":
                self.escuela.listar_estudiantes()
            
            elif opcion == "9":
                self.escuela.listar_maestros()
            
            elif opcion == "10":
                self.escuela.listar_materias()
            
            elif opcion == "11":
                self.escuela.listar_carreras()
            
            elif opcion == "12":
                self.escuela.listar_semestres()
            
            elif opcion == "13":
                self.escuela.listar_grupos()
            
            elif opcion == "14":
                print("\nSeleccionaste: Eliminar estudiante\n")
                numero_control = input("Ingresa el número de control del estudiante: ")
                self.escuela.eliminar_estudiante(numero_control = numero_control)
                
            elif opcion == "15":
                print("\nSeleccionaste: Eliminar maestro")
                numero_control = input("Ingresa el número de control del maestro: ")
                self.escuela.eliminar_maestro(numero_control = numero_control)
            
            elif opcion == "16":
                print("\nSeleccionaste: Eliminar materia")
                id = input("Ingresa el ID de la materia: ")
                self.escuela.eliminar_materia(id = id)
            
            elif opcion == "17":
                print("\n\tAdios basura\n")
                break