from empleados.utils.roles import Rol
from empleados.utils.roles import Tipo_Animal
from empleados.utils.roles import Alimentacion
from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from animal.animal import Animal
from visitante.visitante import Visitante
from visitas.visitas import Visita
from datetime import datetime


class Menu:
    zoo: Zoologico = Zoologico()
    
    def login(self):
        intentos = 0
        
        while intentos < 5:
            print("\n------BIENVENIDO AL SISTEMA DEL ZOOLÓGICO------\n")
            print("Inicia sesión para continuar: ")
            
            id = input("Ingresa el ID de usuario: ")
            contrasena = input("Ingresa la contraseña: ")
            
            usuario = self.zoo.validar_inicio_sesion(id=id, contrasena=contrasena) #Falta hacer el método
            
            if usuario is None:
                intentos = self.mostrar_intentos_sesion_fallidos(intentos_usuario=intentos) #Falta hacer el método
            
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
    1. Registro
    2. Modificar
    3. Asignar mantenimientos
    4. Eliminar
    5. Consultar
    6. Salir
            """
            print(menu)
            
            opcion = int(input("Ingresa una opción para continuar: "))
            
            if opcion == 1:
                print("\nSeleccionaste: Registrar")
                while True:
                    menu_registro = """
    1. Registrar empleado
    2. Registrar animal
    3. Registrar visitantes
    4. Registrar visita
    5. Salir
            """
                    print(menu_registro)
                
                    opcion_registro = int(input("Ingresa una opción para continuar: "))
                    
                    if opcion_registro == 1:
                        print("\nSeleccionaste: Registrar empleado\n")
                    
                        nombre = input("Nombre del empleado: ")
                        apellidos = input("Apellidos: ")
                        ano_ingreso = int(input("Año de ingreso: "))
                        mes_ingreso = int(input("Mes de ingreso: "))
                        dia_ingreso = int(input("Día de ingreso: "))
                        salario = float(input("Ingresa el salario: "))
                        rfc = input("Ingrese RFC: ")
                        curp = input("Ingrese la CURP: ")
                        horario = input("Ingrese el horario del empleado: ")
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        
                        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                        fecha_ingreso = datetime(ano_ingreso, mes_ingreso, dia_ingreso)
                        
                        id, rol = self.zoo.generar_id_empleados(nombre=nombre, ano_nacimiento=ano_nacimiento)
                        print("ID: ", id)

                        empleado = Empleado(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_ingreso=fecha_ingreso, rfc=rfc, curp=curp, salario=salario, horario=horario, id=id, rol=rol)
                        self.zoo.registrar_empleado(empleado = empleado, id = id)
                
                    elif opcion_registro == 2:
                        print("\nSeleccionaste: Registrar animal\n")
                        
                        tipo_animal = Tipo_Animal.validar_animal()
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                        
                        while True:
                            ano_llegada = int(input("Año de ingreso: "))
                            mes_llegada = int(input("Mes de ingreso: "))
                            dia_llegada = int(input("Día de ingreso: "))
                            fecha_llegada_zoo = datetime(ano_llegada, mes_llegada, dia_llegada)
                            
                            if fecha_llegada_zoo >= fecha_nacimiento:
                                break
                            else:
                                print("Fecha de llegada no válida, esta debe ser posterior a la fecha de nacimiento. Intentalo nuevamente.\n")
                        
                        peso = float(input("Peso del animal: "))
                        enfermedades = input("Enfermedades del animal: ")
                        frecuencia_alimentacion = input("Frecuencia de alimentación al día: ")
                        tipo_alimentacion = Alimentacion.validar_tipo_alimentacion()
                        vacunas = bool(input("Cuenta con vacunas 1. Sí / 0. No: "))
                        
                        id = self.zoo.generar_id_animal(tipo_animal=tipo_animal, ano_llegada=ano_llegada, ano_nacimiento=ano_nacimiento)
                        print("ID: ", id)
                        
                        animal = Animal(id=id, tipo_animal=tipo_animal, fecha_nacimiento=fecha_nacimiento, fecha_llegada_zoo=fecha_llegada_zoo, peso=peso, enfermedades=enfermedades, frecuencia_alimentacion=frecuencia_alimentacion, tipo_alimentacion=tipo_alimentacion, vacunas=vacunas)
                        self.zoo.registrar_animal(animal=animal)
                
                    elif opcion_registro == 3:
                        print("\nSeleccionaste: Registrar visitante\n")
                        
                        nombre = input("Nombre: ")
                        apellidos = input("Apellidos: ")
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                        
                        #!numero_visitas += 1
                        curp = input("CURP: ")
                        ano = datetime.now().year
                        mes = datetime.now().month
                        dia = datetime.now().day
                        fecha_registro = datetime(ano, mes, dia)
                        id = self.zoo.generar_id_visitante(ano_nacimiento)
                        print("ID: ", id)
                        visitante = Visitante(id_visitante=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento,numero_visitas=0, curp=curp, fecha_registro=fecha_registro)
                        self.zoo.registrar_visitante(visitante = visitante)
                    
                    elif opcion_registro == 4:
                        print("Seleccionaste: Registrar visita")
                        id = self.zoo.generar_id_visita()
                        print("\nlista de empleados disponibles como Guía:")
                        guia_seleccionado = None
                        while not guia_seleccionado:
                            
                            for guia in Zoologico.lista_guia:
                                print(f"\nID: {guia.id} \nNombre: {guia.nombre} {guia.apellidos}")
                                
                            seleccion = input("\nSelecciona el guía por ID: ")
                            for guia in Zoologico.lista_guia:
                                if seleccion == guia.id:
                                    guia_seleccionado= guia
                                    break
                                
                            
                            if not guia_seleccionado:
                                print("ID de guia no valido, intenta nuevamente.")
                                    
                        visitantes_seleccionados = Visita.visitantes
                        while True:
                            print("\nLista de visitantes registrados: ")
                            for visitante in Zoologico.lista_visitantes:
                                print(f"\nID: {visitante.id_visitante} \nNombre: {visitante.nombre} {visitante.apellidos}")
                                
                            seleccion = input("\nSelecciona el visitante por ID: ")
                            visitante_seleccionado = None
                            for visitante in Zoologico.lista_visitantes:
                                if seleccion == visitante.id_visitante:
                                    visitante_seleccionado= visitante
                                
                                    if visitante_seleccionado == visitantes_seleccionados:
                                        print("\n\tNo se puede registrar dos veces al mismo visitante")
                                        
                                    else:
                                        visitantes_seleccionados.append(visitante_seleccionado)
                                    break
                            if not visitante_seleccionado:
                                print("ID no valido, intenta nuevamente.")
                            else:
                                agregar_otro=input("\nDesea agregar a otro vicitante (s/n): ").lower()
                                if agregar_otro != "s":
                                    break
                                       
                        visita = Visita(id=id, guia=guia_seleccionado, visitantes=visitantes_seleccionados)
                        self.zoo.registrar_visita(visita = visita)
                        print(f"\nVisita registrada con exito. ID: {id}")
                        
                    elif opcion_registro == 5:
                        break
                    
                    else:
                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
            
            elif opcion == 2:
                print("\nSeleccionaste: Modificar\n")
                while True:
                    menu_modificar = """
    1. Modificar empleado
    2. Modificar animal
    3. Modificar visitante
    4. Salir
    """
                    print(menu_modificar)
                
                    opcion_modificar = int(input("Ingresa una opción para continuar: "))
                    
                    if opcion_modificar == 1:
                        id_empleado_modificar = input("ID del empleado: ")
                        for empleado in Zoologico.lista_empleados:
                            if id_empleado_modificar == empleado.id:
                                while True:
                                    menu = """
    MENÚ MODIFICACIONES
    
    1. Nombre
    2. Apellidos
    3. Fecha de nacimiento
    4. Fecha de ingreso
    5. RFC
    6. CURP
    7. Salario
    8. Horario
    9. Salir
                            
                            """
                                    print(menu)
                                    opcion_cambiar = int(input("Dato a modificar: "))
                                    
                                    if opcion_cambiar == 1:
                                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                                        empleado.nombre = nuevo_nombre
                                    
                                    elif opcion_cambiar == 2:
                                        nuevo_apellido = input("Ingresa los nuevos apellidos: ")
                                        empleado.apellidos = nuevo_apellido

                                    elif opcion_cambiar == 3:
                                        nuevo_ano = int(input("Ingresar nuevo año de nacimiento : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de nacimiento : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de nacimiento : "))
                                        nueva_fecha_nacimiento = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        empleado.fecha_nacimiento = nueva_fecha_nacimiento

                                    elif opcion_cambiar == 4:
                                        nuevo_ano = int(input("Ingresar nuevo año de ingreso : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de ingreso : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de ingreso : "))
                                        nueva_fecha_ingreso = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        empleado.fecha_ingreso = nueva_fecha_ingreso

                                    elif opcion_cambiar == 5:
                                        nuevo_rfc = input("Ingresa el nuevo RFC: ")
                                        empleado.rfc = nuevo_rfc

                                    elif opcion_cambiar == 6:
                                        nuevo_curp = input("Ingresa el nuevo CURP: ")
                                        empleado.curp = nuevo_curp

                                    elif opcion_cambiar == 7:
                                        nuevo_salario = float(input("Ingresa el nuevo salario: "))
                                        empleado.salario = nuevo_salario

                                    elif opcion_cambiar == 8:
                                        nuevo_horario = input("Ingrese el nuevo horario: ")
                                        empleado.horario = nuevo_horario

                                    elif opcion_cambiar == 9:
                                        break
                                        
                                    else:
                                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
                                        
                        if not id_empleado_modificar:        
                            print("No se encontro un empleado con el ID: ", id_empleado_modificar)
                                
                    
                    elif opcion_modificar == 2:
                        id_animal_modificar = input("ID del animal: ")
                        for animal in Zoologico.lista_animales:
                            if id_animal_modificar == animal.id:
                                while True:
                                    menu = """
    MENÚ MODIFICACIONES
    
    1. Fecha de nacimiento
    2. Fecha de llegada
    3. Peso
    4. Enfermedades
    5. Frecuancia de alimentación
    6. Vacunas
    7. Salir
                            
                            """
                                    print(menu)
                                    opcion_cambiar = int(input("Dato a modificar: "))
                                    
                                    if opcion_cambiar == 1:
                                        nuevo_ano = int(input("Ingresar nuevo año de nacimiento : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de nacimiento : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de nacimiento : "))
                                        nueva_fecha_nacimiento = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        animal.fecha_nacimiento = nueva_fecha_nacimiento
                                    
                                    elif opcion_cambiar == 2:
                                        nuevo_ano = int(input("Ingresar nuevo año de llegada : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de llegada : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de llegada : "))
                                        nueva_fecha_llegada_zoo = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        animal.fecha_llegada_zoo = nueva_fecha_llegada_zoo

                                    elif opcion_cambiar == 3:
                                        nuevo_peso = float(input("Ingrese el nuevo peso: "))
                                        animal.peso = nuevo_peso

                                    elif opcion_cambiar == 4:
                                        nuevas_enfermedades = input("Ingrese las nuevas enfermedades: ")
                                        animal.enfermedades = nuevas_enfermedades

                                    elif opcion_cambiar == 5:
                                        nueva_frecuencia_alimentacion = input("Ingrese la nueva frecuencia de alimentación: ")
                                        animal.frecuencia_alimentacion = nueva_frecuencia_alimentacion

                                    elif opcion_cambiar == 6:
                                        nuevas_vacunas = bool(input("Cuenta con vacunas 1. Sí / 0. No: "))
                                        animal.vacunas = nuevas_vacunas

                                    elif opcion_cambiar == 7:
                                        break
                                        
                                    else:
                                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
                                        
                        if not id_animal_modificar:        
                            print("No se encontro un animal con el ID: ", id_animal_modificar)
                    
                    elif opcion_modificar == 3:
                        id_visitante_modificar = input("ID del visitante: ")
                        for visitante in Zoologico.lista_visitantes:
                            if id_visitante_modificar == visitante.id_visitante:
                                while True:
                                    menu = """
    MENÚ MODIFICACIONES
    
    1. Nombre
    2. Apellidos
    3. Fecha de nacimiento
    4. Fecha de ingreso
    5. CURP
    6. Salir
                            
                            """
                                    print(menu)
                                    opcion_cambiar = int(input("Dato a modificar: "))
                                    
                                    if opcion_cambiar == 1:
                                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                                        visitante.nombre = nuevo_nombre
                                    
                                    elif opcion_cambiar == 2:
                                        nuevo_apellido = input("Ingresa los nuevos apellidos: ")
                                        visitante.apellidos = nuevo_apellido

                                    elif opcion_cambiar == 3:
                                        nuevo_ano = int(input("Ingresar nuevo año de nacimiento : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de nacimiento : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de nacimiento : "))
                                        nueva_fecha_nacimiento = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        visitante.fecha_nacimiento = nueva_fecha_nacimiento

                                    elif opcion_cambiar == 4:
                                        nuevo_ano = int(input("Ingresar nuevo año de ingreso : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de ingreso : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de ingreso : "))
                                        nueva_fecha_ingreso = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        visitante.fecha_registro = nueva_fecha_ingreso

                                    elif opcion_cambiar == 5:
                                        nuevo_curp = input("Ingresa el nuevo CURP: ")
                                        visitante.curp = nuevo_curp

                                    elif opcion_cambiar == 6:
                                        break
                                        
                                    else:
                                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
                                        
                        if not id_visitante_modificar:        
                            print("No se encontro un visitante con el ID: ", id_visitante_modificar)
                                
                    
                    elif opcion_modificar == 4:
                        break
                    
                    else:
                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
            
            elif opcion == 3:
                pass
            
            elif opcion == 4:
                print("Seleccionaste: Eliminar\n")
                while True:
                    menu_eliminar = """
    1. Eliminar empleado
    2. Eliminar animal
    3. Eliminar visita
    4. Salir
        
                """
                    print(menu_eliminar)
                    opcion_eliminar = int(input("Ingresa una opción para continuar: "))
                    
                    if opcion_eliminar == 1:
                        print("Seleccionaste: Eliminar empleado\n")
                        id = input("Ingresa el ID del empleado a eliminar: ")
                        self.zoo.eliminar_empleado(id = id)
                    
                    elif opcion_eliminar == 2:
                        print("Seleccionaste: Eliminar animal")
                        id = input("Ingresa el ID del animal a eliminar: ")
                        self.zoo.eliminar_animal(id = id)
                    
                    elif opcion_eliminar == 3:
                        print("Seleccionaste: Eliminar visita")
                        id = input("Ingresa el ID de la visita a eliminar: ")
                        self.zoo.eliminar_visita(id = id)
                    
                    elif opcion_eliminar == 4:
                        break
                    
                    else: 
                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
                
            elif opcion == 5:
                print("Seleccionaste: Consultar\n")
                while True:
                    menu_consultar = """
    1. Empleados
    2. Personal veterinario
    3. Personal mantenimiento
    4. Personal guías
    5. Personal administrativo
    6. Animales
    7. Visitantes
    8. Visitas
    9. Salir

                """
                    print(menu_consultar)
                    opcion_consultar = int(input("Ingrese una opción para continuar: "))
                    
                    if opcion_consultar == 1:
                        self.zoo.listar_empleados()
                        
                    elif opcion_consultar == 2:
                        self.zoo.listar_veterinarios()
                        
                    elif opcion_consultar == 3:
                        self.zoo.listar_mantenimiento()
                    
                    elif opcion_consultar == 4:
                        self.zoo.listar_guias()
                    
                    elif opcion_consultar == 5:
                        self.zoo.listar_administrativos()
                        
                    elif opcion_consultar == 6:
                        self.zoo.listar_animales()

                    elif opcion_consultar == 7:
                        self.zoo.listar_visitantes()

                    elif opcion_consultar == 8:
                        self.zoo.listar_visitas()

                    elif opcion_consultar == 9:
                        break
                    
                    else: 
                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
            
            elif opcion == 6:
                break
            
            else:  
                print("\t_////// Esa nos es una opción válida \\\\\\\_\n")