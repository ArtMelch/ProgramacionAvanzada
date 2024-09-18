from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()
menu = """
====== BIENVENIDO AL SISTEMA DEL HOSPITAL ======
    1) Registrar paciente
    2) Registrar médico
    3) Mostrar pacientes
    4) Mostrar medicos
    5) Eliminar paciente
    6) Eliminar médico
    7) Mostrar pacientes menores de edad
    8) Mostrar pacientes mayores de edad
    9) Salir
    
    """

while True: 
    print(menu)
    opcion_user = input("\nSelecciona la opción deseada: ")
    
    if opcion_user == "1":
        print("\nSeleccionaste la opción para registrar un paciente")
        
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        peso = float(input("Ingresa el peso: "))
        estatura = float(input("Ingresa la estatura: "))
        direccion = input("Ingresa la dirección: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("\nPaciente registrado correctamente")
        
    
    elif opcion_user == "2":
        print("\nSeleccionaste la opción para registrar un medico")
        
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        rfc = input("Ingresa el rfc: ")
        direccion = input("Ingresa la dirección: ")
        
        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("\nMedico registrado correctamente")
    
    elif opcion_user == "3":
        hospital.mostrar_pacientes()
        
    elif opcion_user == "4":
        hospital.mostrar_medicos()
    
    elif opcion_user == "5":
        print("\nSeleccionaste la opción para eliminar un paciente")
        id_pac_eliminar = int(input("Ingrese el ID del paciente: "))
        hospital.eliminar_paciente(id_pac_eliminar)
    
    elif opcion_user == "6":
        print("\nSeleccionaste la opción para eliminar un medico")
        id_doc_eliminar = int(input("Ingrese el ID del médico: "))
        hospital.eliminar_medico(id_doc_eliminar)
    
    elif opcion_user == "7":
        hospital.mostrar_pacientes_ninos()
    
    elif opcion_user == "8":
        hospital.mostrar_pacientes_adultos()
    
    elif opcion_user == "9":
        print("\n\tHasta luego")
        break
    
    else:
        print("*****ESA OPCIÓN NO ES VÁLIDA*****")
        
        
# #Parte de la creación y registro de los pacientes
# paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero")
# paciente_dos = Paciente("Pedro", 2006, 68, 1.70, "Avenida Solidaridad")
# paciente_tres = Paciente("Mário", 2010, 50, 1.56, "Avenida Solidaridad")
# hospital.registrar_paciente(paciente = paciente)
# hospital.registrar_paciente(paciente = paciente_dos)
# hospital.registrar_paciente(paciente = paciente_tres)

# #Parte de la creación y registro de los medicos
# medico_uno = Medico("Alberto", 1900, "ALB4917BNDDDF", "Av. Periodismo")
# medico_dos = Medico("Silverio", 1900, "SIV9273BNDDDF", "Av. Héroes")
# hospital.registrar_medico(medico = medico_uno)
# hospital.registrar_medico(medico = medico_dos)

# #Parte donde se muestra la información de los todos los pacientes y medicos
# hospital.mostrar_pacientes()

# hospital.mostrar_medicos()

# #Parte donde muestro los pacientes adultos y niños
# hospital.mostrar_pacientes_adultos()

# hospital.mostrar_pacientes_ninos()

# #Parte donde elimino a uno de los medicos
# id_doc_eliminar = int(input("\nIngrese el ID del medico que quiere eliminar: "))
# hospital.eliminar_medico(id_doc_eliminar)

# hospital.mostrar_medicos()

# #Parte donde elimino a un paciente
# id_pac_eliminar = int(input("\nIngrese el ID del paciente que quiere eliminar: "))
# hospital.eliminar_paciente(id_pac_eliminar)

# hospital.mostrar_pacientes()

# #hospital.registrar_consulta(id_paciente = 1, id_medico = 2) #No registra consulta, pues no hay ni paciente ni medico con dichos ID's