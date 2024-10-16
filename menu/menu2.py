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
                print("\n*Seleccionaste: Registrar*")
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
                        print("\nSelecionaste: Registrar empleado\n")
                    
                        nombre = input("Nombre del empleado: ")
                        apellidos = input("Apellidos: ")
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        salario = float(input("Ingresa el salario: "))
                        rfc = input("Ingrese RFC: ")
                        curp = input("Ingrese la CURP: ")
                        horario = input("Ingrese el horario del empleado: ")
                        while True:
                            ano_ingreso = int(input("Año de ingreso: "))
                            mes_ingreso = int(input("Mes de ingreso: "))
                            dia_ingreso = int(input("Día de ingreso: "))
                            
                            fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                            fecha_ingreso = datetime(ano_ingreso, mes_ingreso, dia_ingreso)
                            
                            if fecha_ingreso > fecha_nacimiento:
                                break
                            else:
                                print("Fecha de ingreso no válida. Inténtalo nuevamente")
                        
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
                                if visitante not in Visita.visitantes:
                                    print(f"\nID: {visitante.id_visitante} \nNombre: {visitante.nombre} {visitante.apellidos}")
                                
                            seleccion = input("\nSelecciona el visitante por ID: ")
                            visitante_seleccionado = None
                            for visitante in Zoologico.lista_visitantes:
                                if seleccion == visitante.id_visitante:
                                    visitante_seleccionado = visitante
                                
                                    if visitante_seleccionado == visitantes_seleccionados:
                                        print("\n\tNo se puede registrar dos veces al mismo visitante")
                                        
                                    else:
                                        visitantes_seleccionados.append(visitante_seleccionado)
                                        visitante =+ 1
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
                print("\n*Seleccionaste: Modificar\n*")
                while True:
                    menu_modificar = """
        1. Modificar empleado
        2. Modificar animal
        3. Modificar visitantes
        4. Modificar visita
        5. Salir
        """
                    print(menu_modificar)
                
                    opcion_modificar = int(input("Ingresa una opción para continuar: "))
                    
                    if opcion_modificar == 1:
                        pass
                    elif opcion_modificar == 2:
                        pass
                    elif opcion_modificar == 3:
                        pass
                    elif opcion_modificar == 4:
                        pass
                    elif opcion_modificar == 5:
                        pass
                    
                    else:
                        print("\t_////// Esa nos es una opción válida \\\\\\\_\n")
            
            elif opcion == 3:
                    print("Seleccionaste: Asignar mantenimientos")
    
                    print("\nLista de empleados disponibles para mantenimiento:")
                    empleado_seleccionado = None
                    while not empleado_seleccionado:
                        for empleado in Zoologico.lista_empleados:
                            if empleado.rol == Rol.MANTENIMIENTO:
                                print(f"ID: {empleado.id}, Nombre: {empleado.nombre} {empleado.apellidos}")
                        
                        seleccion_empleado = input("Selecciona el empleado por ID: ")
                        
                        for empleado in Zoologico.lista_empleados:
                            if seleccion_empleado == empleado.id and empleado.rol == Rol.MANTENIMIENTO:
                                empleado_seleccionado = empleado
                                break
                        if not empleado_seleccionado:
                            print("ID de empleado no válido o el empleado no tiene rol de Mantenimiento. Intenta nuevamente.")
                            
                    id_animal = input("Ingresa el ID del animal: ")
                    
                    # Solicitar tipo de proceso
                    print("\nSelecciona el tipo de proceso:")
                    print("1. Alimentación")
                    print("2. Limpieza")
                    print("3. Mantenimiento")
                    tipo_proceso = input("Opción: ")
                    
                    if tipo_proceso == "1":
                        proceso = "Alimentación"
                    elif tipo_proceso == "2":
                        proceso = "Limpieza"
                    elif tipo_proceso == "3":
                        proceso = "Mantenimiento"
                    else:
                        print("Opción no válida. Se asignará el proceso como 'Mantenimiento'.")
                        proceso = "Mantenimiento"
                    
                    fecha_proceso = datetime.now().strftime("%Y-%m-%d")
                    observaciones = input("Ingresa observaciones (opcional, presiona Enter si no hay): ")
                    
                    registro_proceso = {
                        "empleado": empleado_seleccionado,
                        "id_animal": id_animal,
                        "proceso": proceso,
                        "fecha_proceso": fecha_proceso,
                        "observaciones": observaciones
                    }
                    
                    Zoologico.procesos_realizados.append(registro_proceso)
                    
                    print(f"\nProceso de {proceso} registrado exitosamente para el animal con ID: {id_animal}.")
            
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