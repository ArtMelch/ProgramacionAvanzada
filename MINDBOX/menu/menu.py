from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carreras.carrera import Carrera
from semestres.semestre import Semestre
from grupos.grupo import Grupo
from usuario.utils.roles import Rol
from coordinador.coordinador import Coordinador
from datetime import datetime


class Menu:
    escuela = Escuela()
    
    
    def login(self):
        intentos = 0
        
        while intentos < 5:
            print("\n----BIENVENIDO----\n")
            print("Inicia sesión para continuar")
            
            numero_control = input("\nIngresa tu número de control: ")
            contrasena_usuario = input("Ingresa tu contraseña: ")
            
            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, constrasena=contrasena_usuario)
            
            if usuario is None:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            
            else:
                if usuario.rol == Rol.ESTUDIANTE:
                    self.mostrar_menu_estudiante(usuario)
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    self.mostrar_menu_maestro(usuario)
                    intentos = 0
                else: 
                    self.mostrar_menu(usuario)
                    intentos = 0
            
        print("\nMáximos intentos permitidos. Adios basura")
    
    
    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("\nUsuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1
    
    def mostrar_menu_estudiante(self, usuario: Estudiante):
        print("MENÚ DEL ESTUDIANTE")
        opcion = 0
        while opcion != 5:
            menu1 = """
                MINDBOX
                1. Ver horarios
                2. Ver grupos
                3. Ver materias
                4. Ver mi infomación
                5. Salir   
            """
            #! AGREGAR MÁS OPCIONES
            print(menu1)
            opcion = int(input("Ingresa una opción: "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                print("\n-------MI INFORMACIÓN---------")
                print(usuario.mostrar_info_est())
                
            elif opcion == 5:
                break
            
            
    
    def mostrar_menu_maestro(self, usuario:Maestro):
        print("MENÚ DEL MAESTRO")
        opcion = 0
        while opcion != 6:
            menu1 = """
                MINBOX
                1. Ver horarios
                2. Ver grupos
                3. Ver materias
                4. Ver alumnos
                5. Ver mi información
                6. Salir 
            """
            #! AGREGAR MÁS OPCIONES
            print(menu1)
            opcion = int(input("Ingresa una opción: "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                print("\n-------MI INFORMACIÓN---------")
                print(usuario.mostrar_info_mtr())
                
            elif opcion == 6:
                break
    
    def mostrar_menu(self, usuario: Coordinador):
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
    
    17) Ver mi información
    18) Salir

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
                print("Número de control: ", numero_control)
                maestro = Maestro(numero_control=numero_control,nombre=nombre, apellido=apellido, ano_nacimiento=ano_nacimiento, rfc=rfc, sueldo=sueldo, contrasena=contrasena)
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
                print("\n-------MI INFORMACIÓN---------")
                print(usuario.mostrar_info_coor())
            
            elif opcion == "18":
                print("\n\tAdios basura\n")
                break