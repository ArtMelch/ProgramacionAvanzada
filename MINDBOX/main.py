from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime

escuela = Escuela()

menu = """
___________MINDBOXS__________

    1) Registrar estudiante
    2) Registrar maestro
    3) Regristrar grupo
    4) Registrar materia
    5) Registrar horario
    6) Salir

"""

while True:
    print(menu)
    opcion = input("Ingresa una opción para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste la opción para registrar un estudiante")
        
        numero_control = escuela.generar_numero_control_est()
        print(numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa el curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el día de nacimiento del estudiante: "))
        
        fecha_nacimiento = datetime(ano, mes, dia)
        escuela.registrar_estudiante(estudiante = Estudiante)
        
    elif opcion == "2":
        print("\nSeleccionaste la opción para registrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el RFC del maestro: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        
        numero_control = escuela.generar_numero_control_mtro(nombre, rfc, ano_nacimiento)
        print(numero_control)
        escuela.registrar_maestro(maestro = Maestro)
        
        
    elif opcion == "3":
        pass
    
    elif opcion == "4":
        print("Seleccionaste Registrar materia")
        nombre = input("Ingresa el nombre del la materia: ")
        descripcion = input("Ingresa la descripción de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa el número de créditos del semestre: "))
        
        id = escuela.generar_id_materia(nombre, semestre, creditos)
        print("ID de la materia: ",id)
        escuela.registrar_materia(materia = Materia)
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        print("\n\tAdios basura\n")
        break