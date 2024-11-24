import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *


def login():
    usuario = user_entry.get()
    contrasena = contra_entry.get()
    
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',  database='biblioteca')
        cursor = conn.connect()
        cursor = conn.cursor()   
        cursor.execute('''
            SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s  ''', (usuario, contrasena))
 
        usuario = cursor.fetchone()
        
        if usuario:
            messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[3]}.")
            validacion(usuario=usuario)
            
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
    
    finally:
        if conn.is_connected():
            conn.close() 
    
def validacion(usuario):
    if usuario[5] == "Administrador":
        ventana_admin()
        
    elif usuario[5] == "Empleado":
        ventana_empleado()
    
def filtrar():
    print("Se filtró")

def ventana_empleado():
    vent_principal.withdraw()
    
    def cerrar_sesion():
        vent_empleado.destroy()
        vent_principal.deiconify()
        user_entry.delete(0, tk.END)
        contra_entry.delete(0,tk.END)
    
    def mostrar():
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="biblioteca")
        micursor=mysqlC.cursor()
        micursor.execute("SELECT * FROM libros")
        lista = micursor.fetchall()
        
        for i,(id, titulo, autor, edit, ano_publi, precio) in enumerate(lista, start=0):
            listbox.insert("","end",values=(id,titulo,autor,edit,ano_publi,precio))
            mysqlC.close()
            
    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()
        
    def agregar():
        idAdd = id_entry.get()
        tituloAdd = titulo_entry.get()
        autorAdd = autor_entry.get()
        editAdd = edit_entry.get()
        ano_publiAdd = ano_publi_entry.get()
        precioAdd = precio_entry.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password= "", database= "biblioteca") 
        micursor = mysqlC.cursor()
    
        try:
            micursor.execute(f"INSERT INTO libros(id, titulo, autor, editorial, año_Publi, precio) values('{idAdd}','{tituloAdd}','{autorAdd}','{editAdd}','{ano_publiAdd}','{precioAdd}')")
            mysqlC.commit()
            id_entry.delete(0,tk.END)
            titulo_entry.delete(0,tk.END)
            autor_entry.delete(0,tk.END)
            edit_entry.delete(0,tk.END)
            ano_publi_entry.delete(0,tk.END)
            precio_entry.delete(0,tk.END)
            messagebox.showinfo("Información", "Libro agregado")
            
        except Exception as e:
            print(e)
            mysqlC.rollback() # Rolllback: Todo lo que ejecutaste regresalo, se hace todo o no se hace nada
            mysqlC.close() #Cierra la conexión con la base de datos
        actualizar()
        
    def eliminar():
        idAdd = id_entry.get()
        mysqlC= mysql.connector.connect(host='localhost', user='root', password='', database='biblioteca')
        micursor =mysqlC.cursor()
        try:
            micursor.execute(f"DELETE FROM libros WHERE id={idAdd}")
            mysqlC.commit()
            id_entry.delete(0,tk.END)
            titulo_entry.delete(0,tk.END)
            autor_entry.delete(0,tk.END)
            edit_entry.delete(0,tk.END)
            ano_publi_entry.delete(0,tk.END)
            precio_entry.delete(0,tk.END)
            
            messagebox.showinfo("Información", "Libro eliminado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback() 
            mysqlC.close() 
    
    def editar():
        idAdd = id_entry.get()
        tituloAdd = titulo_entry.get()
        autorAdd = autor_entry.get()
        editAdd = edit_entry.get()
        ano_publiAdd = ano_publi_entry.get()
        precioAdd = precio_entry.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password= "", database= "biblioteca") 
        micursor = mysqlC.cursor()
        
        try:
            micursor.execute(f"UPDATE libros SET titulo='{tituloAdd}', autor='{autorAdd}', editorial='{editAdd}', año_publi='{ano_publiAdd}', precio='{precioAdd}' WHERE id='{idAdd}'")
            mysqlC.commit()
            id_entry.delete(0,tk.END)
            titulo_entry.delete(0,tk.END)
            autor_entry.delete(0,tk.END)
            edit_entry.delete(0,tk.END)
            ano_publi_entry.delete(0,tk.END)
            precio_entry.delete(0,tk.END)
            
            messagebox.showinfo("Información", "Libro editado")
            actualizar()
            
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
    
    def obtenerR(event):
        id_entry.delete(0,tk.END)
        titulo_entry.delete(0,tk.END)
        autor_entry.delete(0,tk.END)
        edit_entry.delete(0,tk.END)
        ano_publi_entry.delete(0,tk.END)
        precio_entry.delete(0,tk.END)
        
        renglon = listbox.selection()[0] 
        seleccion = listbox.set(renglon)
        id_entry.insert(0,seleccion["Id"])
        titulo_entry.insert(0,seleccion["Título"])
        autor_entry.insert(0,seleccion["Autor"])
        edit_entry.insert(0,seleccion["Editorial"])
        ano_publi_entry.insert(0,seleccion["Año de publicación"])
        precio_entry.insert(0,seleccion["Precio"])
        
    #! VENTANA EMPLEADO
    vent_empleado = tk.Toplevel(vent_principal)
    vent_empleado.title("Empleado")
    vent_empleado.geometry("820x500")
    
    global id_entry
    global titulo_entry
    global autor_entry
    global edit_entry
    global ano_publi_entry
    global precio_entry
    
    #?Labels
    label2 = tk.Label(vent_empleado,text="Gestión de libros en el inventario",font=("Arial",14), fg="blue")
    label2.place(x=300,y=10)
    id_label = tk.Label(vent_empleado,text="ID:", font=("Arial",12))
    id_label.place(x=15,y=40)
    titulo_label = tk.Label(vent_empleado, text="Titulo:", font=("Arial",12))
    titulo_label.place(x=15,y=60)
    autor_label = tk.Label(vent_empleado, text="Autor:", font=("Arial",12))
    autor_label.place(x=15,y=80)
    edit_label = tk.Label(vent_empleado, text="Editorial:", font=("Arial",12))
    edit_label.place(x=15,y=100)
    ano_publi_label = tk.Label(vent_empleado, text="Año de publicación:", font=("Arial",12))
    ano_publi_label.place(x=15,y=120)
    precio_label =tk.Label(vent_empleado, text="Precio:", font=("Arial",12))
    precio_label.place(x=15,y=140)
    filtrar_label = tk.Label(vent_empleado, text="Filtrar por año de publicación", font=("Arial",13))
    filtrar_label.place(x=510, y=70)

    #?Entry
    id_entry = tk.Entry(vent_empleado)
    id_entry.place(x=200, y=40)
    titulo_entry = tk.Entry(vent_empleado)
    titulo_entry.place(x=200, y=60)
    autor_entry = tk.Entry(vent_empleado)
    autor_entry.place(x=200, y=80)
    edit_entry = tk.Entry(vent_empleado)
    edit_entry.place(x=200, y=100)
    ano_publi_entry = tk.Entry(vent_empleado)
    ano_publi_entry.place(x=200, y=120)
    precio_entry = tk.Entry(vent_empleado)
    precio_entry.place(x=200, y=140)
    filtrar_entry = tk.Entry(vent_empleado, font=("Arial",11))
    filtrar_entry.place(x=570,y=100)
    
    #? Buttons
    tk.Button(vent_empleado,text="Agregar",command=agregar, height=5, width=10, font=("Arial",12)).place(x=50,y=170)
    tk.Button(vent_empleado,text="Editar",command=editar, height=5, width=10, font=("Arial",12)).place(x=200,y=170)
    tk.Button(vent_empleado,text="Eliminar",command=eliminar, height=5, width=10, font=("Arial",12)).place(x=350,y=170)
    tk.Button(vent_empleado,text="Buscar", command=filtrar, font=("Arial",11)).place(x=500,y=100)
    tk.Button(vent_empleado,text="Cerrar sesión", command=cerrar_sesion, font=("Arial",13), fg="red").place(x=550,y=200)
    
    columnas = ("Id", "Título", "Autor", "Editorial","Año de publicación", "Precio")
    listbox = ttk.Treeview(vent_empleado, columns=columnas, show="headings")
    
    listbox.column("Id",width=40)
    listbox.column("Título",width=300)
    listbox.column("Autor",width=200)
    listbox.column("Editorial",width=80)
    listbox.column("Año de publicación",width=120)
    listbox.column("Precio",width=80)
    
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=280)
    
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    
 #! Ventana Admin       
def ventana_admin():
    def eliminar_empleado_ventana():
        def cargar_empleados():
            try:
                mysql_c = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='biblioteca'
                )
                micursor = mysql_c.cursor()
                micursor.execute("SELECT ID, Nombre, Apellido, Usuario, Rol FROM usuarios")
                rows = micursor.fetchall()

                for item in tree.get_children():
                    tree.delete(item)

                for row in rows:
                    tree.insert("", tk.END, values=row)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo cargar la lista de empleados: {err}")

            finally:
                if 'mysql_c' in locals() and mysql_c.is_connected():
                    mysql_c.close()

        def eliminar_empleado():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showerror("Error", "Por favor, selecciona un empleado para eliminar")
                return

            item = tree.item(selected_item[0], "values")
            idEliminar = item[0] 

            confirmacion = messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar al empleado con ID {idEliminar}?")
            if not confirmacion:
                return

            try:
                mysql_c = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='biblioteca'
                )
                micursor = mysql_c.cursor()

                consulta = "DELETE FROM usuarios WHERE ID=%s"
                micursor.execute(consulta, (idEliminar,))
                mysql_c.commit()

                messagebox.showinfo("Información", "Empleado eliminado correctamente")
                cargar_empleados() 

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo eliminar al empleado: {err}")

            finally:
                if 'mysql_c' in locals() and mysql_c.is_connected():
                    mysql_c.close()

        root = tk.Toplevel(vent_principal)
        root.title("Eliminar Empleado")
        root.geometry("800x400")

        tk.Label(root, text="Eliminar Empleado", fg="red", font=("Arial", 28)).place(x=100, y=140)

        columns = ("ID", "Nombre", "Apellido", "Usuario", "Rol")
        tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        tk.Button(root, text="Eliminar Empleado", command=eliminar_empleado, height=2, width=20, font=("Arial", 12)).pack(pady=10)

        cargar_empleados()
    def cerrar_sesion():
        vent_admin.destroy()
        vent_principal.deiconify()
        user_entry.delete(0, tk.END)
        contra_entry.delete(0,tk.END)
    def reg_emple():
        global nombre, apellido, contraseña, usuario, identificador
        
        root = tk.Toplevel(vent_principal)
        root.title("Registro de Empleados")
        root.geometry("600x400")
        
        tk.Label(root, text="Registro de Empleados", fg="red", font=("Arial", 28)).pack(pady=10)
        
        etiquetas = ["ID", "Nombre", "Apellido", "Usuario", "Contraseña"]
        y_positions = [50, 80, 110, 140, 170]
        
        for etiqueta, y in zip(etiquetas, y_positions):
            tk.Label(root, text=etiqueta, font=("Arial", 12)).place(x=100, y=y)
        
        identificador = tk.Entry(root)
        identificador.place(x=270, y=50)
        nombre = tk.Entry(root)
        nombre.place(x=270, y=80)
        apellido = tk.Entry(root)
        apellido.place(x=270, y=110)
        usuario = tk.Entry(root)
        usuario.place(x=270, y=140)
        contraseña = tk.Entry(root, show="*")
        contraseña.place(x=270, y=170)
        
        
        tk.Button(root, text="Registrar como Administrador", command=lambda: add(root,"Administrador"), height=2, width=25, font=("Arial", 12)).place(x=170, y=220)
        tk.Button(root, text="Registrar como Empleado", command=lambda: add(root, "Empleado"), height=2, width=25, font=("Arial", 12)).place(x=170, y=270)
        
        root.mainloop()

    def add(root, rol):
        idAdd = identificador.get().strip()
        nombreAdd = nombre.get().strip()
        apellidoAdd = apellido.get().strip()
        userAdd = usuario.get().strip()
        contraAdd = contraseña.get().strip()

        if not (idAdd and nombreAdd and apellidoAdd and userAdd and contraAdd):
            messagebox.showerror("Error", "Todos los campos deben estar llenos")
            return

        try:
            mysql_c = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='biblioteca'
            )
            micursor = mysql_c.cursor()

            consulta = """INSERT INTO usuarios (ID, Nombre, Apellido, Usuario, Contraseña, Rol) VALUES (%s, %s, %s, %s, %s, %s)"""
            valores = (idAdd, nombreAdd, apellidoAdd, userAdd, contraAdd, rol)

            micursor.execute(consulta, valores)
            mysql_c.commit()

            identificador.delete(0, tk.END)
            nombre.delete(0, tk.END)
            apellido.delete(0, tk.END)
            usuario.delete(0, tk.END)
            contraseña.delete(0, tk.END)

            messagebox.showinfo("Información", f"Usuario registrado como {rol} correctamente")
            
            root.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar el usuario: {err}")

        finally:
            if 'mysql_c' in locals() and mysql_c.is_connected():
                mysql_c.close()

    def editar_emple():
        def cargar_empleados():
            try:
                mysql_c = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='biblioteca'
                )
                micursor = mysql_c.cursor()
                micursor.execute("SELECT ID, Nombre, Apellido, Usuario, Rol FROM usuarios")
                rows = micursor.fetchall()

                for item in tree.get_children():
                    tree.delete(item)

                for row in rows:
                    tree.insert("", tk.END, values=row)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo cargar la lista de empleados: {err}")

            finally:
                if 'mysql_c' in locals() and mysql_c.is_connected():
                    mysql_c.close()

        def on_double_click(event):
            item = tree.selection()[0] 
            values = tree.item(item, "values") 

            idEdit, nombreEdit,apellidoEdit, usuarioEdit, rolEdit = values

            
            editar_empleado_ventana(idEdit, nombreEdit,apellidoEdit, usuarioEdit, rolEdit)

        def editar_empleado_ventana(idEdit, nombreEdit,apellidoEdit, usuarioEdit, rolEdit):
            def actualizar_emple():
                nombreNuevo = nombre.get().strip()
                apellidoNuevo = apellido.get().strip()
                usuarioNuevo = usuario.get().strip()
                contraNuevo = contraseña.get().strip()
                rolNuevo = rol_combobox.get().strip()

                if not (nombreNuevo and apellidoNuevo and usuarioNuevo and rolNuevo):
                    messagebox.showerror("Error", "Todos los campos (excepto Contraseña) deben estar llenos")
                    return

                try:
                    mysql_c = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='biblioteca'
                    )
                    micursor = mysql_c.cursor()

                    if not contraNuevo:
                        micursor.execute("SELECT Contraseña FROM usuarios WHERE ID=%s", (idEdit,))
                        contraNuevo = micursor.fetchone()[0]

                    consulta = """
                    UPDATE usuarios 
                    SET Nombre=%s, Apellido=%s, Usuario=%s, Contraseña=%s, Rol=%s
                    WHERE ID=%s
                    """
                    valores = (nombreNuevo, apellidoNuevo, usuarioNuevo, contraNuevo, rolNuevo, idEdit)
                    micursor.execute(consulta, valores)
                    mysql_c.commit()

                    messagebox.showinfo("Información", "Empleado actualizado correctamente")
                    root.destroy()
                    cargar_empleados()  

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"No se pudo actualizar al empleado: {err}")

                finally:
                    if 'mysql_c' in locals() and mysql_c.is_connected():
                        mysql_c.close()


            root = tk.Toplevel(vent_principal)
            root.title("Editar Empleado")
            root.geometry("600x400")

            tk.Label(root, text="Editar Información del Empleado", fg="red", font=("Arial", 28)).pack(pady=10)

            etiquetas = ["Nombre", "Apellido", "Usuario", "Contraseña", "Rol"]
            y_positions = [80, 110, 140, 170, 200]

            global nombre, apellido, usuario, contraseña, rol_combobox

            for etiqueta, y in zip(etiquetas, y_positions):
                tk.Label(root, text=etiqueta, font=("Arial", 12)).place(x=100, y=y)

            nombre = tk.Entry(root)
            nombre.place(x=270, y=80)
            nombre.insert(0, nombreEdit)

            apellido = tk.Entry(root)
            apellido.place(x=270, y=110)
            apellido.insert(0, apellidoEdit)

            usuario = tk.Entry(root)
            usuario.place(x=270, y=140)
            usuario.insert(0, usuarioEdit) 

            contraseña = tk.Entry(root, show="*")
            contraseña.place(x=270, y=170)

            rol_combobox = ttk.Combobox(root, values=["Administrador", "Empleado"])
            rol_combobox.place(x=270, y=200)
            rol_combobox.set(rolEdit) 

            tk.Button(root, text="Actualizar Empleado", command=actualizar_emple, height=2, width=25, font=("Arial", 12)).place(x=170, y=250)

        root = tk.Toplevel(vent_principal)
        root.title("Lista de Empleados")
        root.geometry("800x400")

        tk.Label(root, text="Lista de Empleados", fg="red", font=("Arial", 28)).pack(pady=10)

        columns = ("ID", "Nombre", "Apellido", "Usuario", "Rol")
        tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        cargar_empleados()

        tree.bind("<Double-1>", on_double_click)
    
    vent_principal.withdraw()
    
    vent_admin = tk.Toplevel(vent_principal)
    vent_admin.title("Administrador")
    vent_admin.geometry("300x300")
        
    label2 = tk.Label(vent_admin,text="Buenos dias Administrador")
    label2.place(x=100, y=10)

    inicio_boton = tk.Button(vent_admin, text="Registrar Empleado",command=reg_emple)
    inicio_boton.place(x=90,y=100)
    
    editar_boton = tk.Button(vent_admin, text="Editar Empleado", command=editar_emple)
    editar_boton.place(x=90, y=130)
    
    cerrar_boton = tk.Button(vent_admin, text="Cerrar Sesion",command=cerrar_sesion)
    cerrar_boton.place(x=90,y=190)
    
    eliminar_boton = tk.Button(vent_admin, text="Eliminar Empleado", command=eliminar_empleado_ventana)
    eliminar_boton.place(x=90, y=160)
    
    
#? VENTANA PRINCIPAL 
vent_principal = tk.Tk()
vent_principal.title("Sistema de gestión")
vent_principal.geometry("300x300")

label1 = tk.Label(vent_principal, text="Inicio de sesión")
label1.place(x=100, y=10)

user_label = tk.Label(vent_principal, text="Usuario:")
user_label.place(x=70, y=40)
user_entry = tk.Entry(vent_principal)
user_entry.place(x=120, y=40)

contra_label = tk.Label(vent_principal, text="Contraseña:")
contra_label.place(x=50, y=70)
contra_entry = tk.Entry(vent_principal, show="*")
contra_entry.place(x=120, y=70)

inicio_boton = tk.Button(vent_principal, text="Iniciar sesión",command=login)
inicio_boton.place(x=130,y=100)


vent_principal.mainloop()