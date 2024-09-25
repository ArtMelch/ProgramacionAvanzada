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
    6) Mostrar estudiantes
    7) Mostrar maestros
    8) Mostrar materias
    9) Mostrar grupos
    10) Eliminar estudiante
    11) Eliminar maestro
    12) Eliminar materia
    13) Salir

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
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante = estudiante)
        
    elif opcion == "2":
        print("\nSeleccionaste la opción para registrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el RFC del maestro: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        
        numero_control = escuela.generar_numero_control_mtro(nombre, rfc, ano_nacimiento)
        print(numero_control)
        maestro = Maestro(nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
        escuela.registrar_maestro(maestro = maestro)
        
        
    elif opcion == "3":
        pass
    
    elif opcion == "4":
        print("\nSeleccionaste -Registrar materia")
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripción de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa el número de créditos del semestre: "))
        
        id = escuela.generar_id_materia(nombre, semestre, creditos)
        print(id)
        materia = Materia(id=id, nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
        escuela.registrar_materia(materia = materia)
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        escuela.listar_estudiantes()
    
    elif opcion == "7":
        escuela.listar_maestros()
    
    elif opcion == "8":
        escuela.listar_materias()
    
    elif opcion == "9":
        pass
    
    elif opcion == "10":
        print("\nSeleccionaste la opción para eliminar un estudiante")
        numero_control = input("Ingresa el número de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control = numero_control)
        
    elif opcion == "11":
        print("\nSeleccionaste la opción para eliminar un maestro")
        numero_control = input("Ingresa el número de control del maestro: ")
        escuela.eliminar_maestro(numero_control = numero_control)
    
    elif opcion == "12":
        print("\nSeleccionaste la opción para eliminar una materia")
        id = input("Ingresa el ID de la materia: ")
        escuela.eliminar_materia(id = id)
    
    elif opcion == "13":
        print("\n\tAdios basura\n")
        break