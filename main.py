from paciente import Paciente
from hospital import Hospital
from medico import Medico

hospital = Hospital()

#Parte de la creación y registro de los pacientes
paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero")
paciente_dos = Paciente("Pedro", 2006, 68, 1.70, "Avenida Solidaridad")
paciente_tres = Paciente("Mário", 2010, 50, 1.56, "Avenida Solidaridad")
hospital.registrar_paciente(paciente = paciente)
hospital.registrar_paciente(paciente = paciente_dos)
hospital.registrar_paciente(paciente = paciente_tres)

#Parte de la creación y registro de los medicos
medico_uno = Medico("Alberto", 1900, "ALB4917BNDDDF", "Av. Periodismo")
medico_dos = Medico("Silverio", 1900, "SIV9273BNDDDF", "Av. Héroes")
hospital.registrar_medico(medico = medico_uno)
hospital.registrar_medico(medico = medico_dos)

#Parte donde se muestra la información de los todos los pacientes y medicos
hospital.mostrar_pacientes()

hospital.mostrar_medicos()

#Parte donde muestro los pacientes adultos y niños
hospital.mostrar_pacientes_adultos()

hospital.mostrar_pacientes_ninos()

#Parte donde elimino a uno de los medicos
id_doc_eliminar = int(input("\nIngrese el ID del medico que quiere eliminar: "))
hospital.eliminar_medico(id_doc_eliminar)

hospital.mostrar_medicos()

#Parte donde elimino a un paciente
id_pac_eliminar = int(input("\nIngrese el ID del paciente que quiere eliminar: "))
hospital.eliminar_paciente(id_pac_eliminar)

hospital.mostrar_pacientes()

#hospital.registrar_consulta(id_paciente = 1, id_medico = 2) #No registra consulta, pues no hay ni paciente ni medico con dichos ID's