import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
import mysql.connector
from usuarios.usuarios import Usuarios
from tkinter import *

global nombre
global apellido
global password
global usuario
global identificador

def reg_emple():
    
    nombreoAdd= nombre.get()
    apelliAdd= apellido.get()
    usuarioAdd= usuario.get()
    contraAdd= password.get()
    idAdd= identificador.get()
    mysqlC =mysql.connector.connect(host='localhost',user='root',password='',database='biblioteca')
    micursor = mysqlC.cursor()

    try:
        micursor.execute(f"insert into usuarios(ID,Nombre,Apellido,Usuario,Contraseña) values('{idAdd}','{nombreoAdd}','{apelliAdd}','{usuarioAdd}','{contraAdd}')")
        mysqlC.commit()
        nombre.delete(0,END)
        apellido.delete(0,END)
        usuario.delete(0,END)
        password.delete(0,END)
        identificador.delete(0,END)
        
        messagebox.showinfo("Información","Usuario agregado")
        
        
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()
        
    

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
    
        
def ventana_admin():
    vent_principal.withdraw()
    
    vent_admin = tk.Toplevel(vent_principal)
    vent_admin.title("Administrador")
    vent_admin.geometry("300x300")
        
    label2 = tk.Label(vent_admin,text="Buenos dias Administrador")
    label2.place(x=100, y=10)

    inicio_boton = tk.Button(vent_admin, text="Registrar Empleado",command=reg_emple)
    inicio_boton.place(x=130,y=100)
    
    
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