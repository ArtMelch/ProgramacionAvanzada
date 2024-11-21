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
        vent_empleado = tk.Toplevel(vent_principal)
        vent_empleado.title("Empleado")
        vent_empleado.geometry("300x300")
        
def ventana_admin():
    vent_principal.withdraw()
    
    vent_admin = tk.Toplevel(vent_principal)
    vent_admin.title("Administrador")
    vent_admin.geometry("300x300")
        
    label2 = tk.Label(vent_admin,text="Buenos dias Administrador")
    label2.place(x=100, y=10)

    inicio_boton = tk.Button(vent_admin, text="Registrar Empleado",command=reg_emple)
    inicio_boton.place(x=130,y=100)
    
vent_principal = tk.Tk()
vent_principal.title("Sistema de gestión")
vent_principal.geometry("300x300")


label1 = tk.Label(vent_principal,text="Inicio de sesión")
label1.place(x=100, y=10)

user_label = tk.Label(vent_principal, text="Usuario:")
user_label.place(x=70, y=40)
user_entry = tk.Entry(vent_principal)
user_entry.place(x=120, y=40)

contra_label = tk.Label(vent_principal, text="Contraseña:")
contra_label.place(x=50, y=70)
contra_entry = tk.Entry(vent_principal)
contra_entry.place(x=120, y=70)

inicio_boton = tk.Button(vent_principal, text="Iniciar sesión",command=login)
inicio_boton.place(x=130,y=100)


vent_principal.mainloop()


    
    