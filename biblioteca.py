import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from usuarios.usuarios import Usuarios
from tkinter import *


def reg_emple():
    global nombre, apellido, contraseña, usuario, identificador
    
    root = tk.Tk()
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
    
    
    tk.Button(root, text="Registrar como Administrador", command=lambda: add("Administrador"), height=2, width=25, font=("Arial", 12)).place(x=170, y=220)
    tk.Button(root, text="Registrar como Empleado", command=lambda: add("Empleado"), height=2, width=25, font=("Arial", 12)).place(x=170, y=270)
    
    root.mainloop()

def add(rol):
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

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo agregar el usuario: {err}")

    finally:
        if 'mysql_c' in locals() and mysql_c.is_connected():
            mysql_c.close()

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


    
    