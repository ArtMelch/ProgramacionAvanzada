import tkinter as tk
from typing import List
from tkinter import *

class Producto:
    nombre: str
    precio: float
    cantidad: int
    valor_total: float
    
    def __init__(self, nombre:str, precio:float, cantidad:int, valor_total: float):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.valor_total = valor_total
        
    
    def inventario_valor_total(producto):
        valor_t_inv = 0
        for producto in lista_productos:
            valor_t_inv = float(valor_t_inv + producto.valor_total)
            
        label_total.config(text=f"${valor_t_inv}")
        
    def mostrar_detalles(nombre, precio, cantidad, valor_total):
        texto.insert("1.0",f" DETALLES \n Nombre del producto: {nombre} \n Precio: {precio} \n Cantidad: {cantidad} \n Valor total: {valor_total}")

class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def agregar_producto():
    
    def actualizar_detalles():
        Producto.mostrar_detalles(nombre=nombre, precio=precio, cantidad=cantidad, valor_total=valor_total)
        
    def actualizar_total():
        Producto.inventario_valor_total(producto)
        
    
    boton_mostrar_info = tk.Button(ventana, text="Detalles del producto agregado", font=("Courier", 10), command=actualizar_detalles)
    boton_mostrar_info.grid(row=5, column=0, padx=5)
    
    boton_total = tk.Button(ventana, text="Actualizar total", font=("Courier", 10), command=actualizar_total)
    boton_total.grid(row=4, column=1)
    
    
    try:
        nombre = str(entry_nombre.get())
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
        
        escribirNombre(nombre=nombre)
        escribirPrecio(precio=precio)
        escribirCantidad(cantidad=cantidad)
        
        valor_total = round(float(precio * cantidad), 3)
    
        producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad, valor_total=valor_total)
        lista_productos.append(producto)
        
        label_error.config(text="")
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        texto.delete("1.0",tk.END)
        
    except MiError as e:
        label_error.config(text=e, font=("Consolas", 8,"bold"), fg="Red")
    except ValueError:
        label_error.config(text="El precio o la cantidad tienen \n algo diferente a un número", font=("Consolas", 8,"bold"), fg="Red")
      
    
    
def escribirNombre(nombre):
    if (nombre == ""):
        raise MiError("Nombre invalido, debe poner al menos \n un caracter")
    
def escribirPrecio(precio):
    if (precio <= 0):
        raise MiError("Precio invalido, debe ser mayor a cero")
    
def escribirCantidad(cantidad):
    if (cantidad < 0):
        raise MiError("Cantidad invalida, debe ser mayor \n o igual a cero")
    

lista_productos: List[Producto] = []
            
ventana = tk.Tk()
ventana.title("Gestión de inventario")
ventana.geometry("500x500")
ventana.configure(bg="lightblue")
ventana.attributes("-alpha",0.95)

boton_crear_producto = tk.Button(ventana, text="Agregar producto", font=("Courier", 10), command=agregar_producto)
boton_crear_producto.grid(row=3, column=1, padx=5)

label_nombre = tk.Label(ventana, text="Nombre del producto: ", font=("Times", 11), bg="lightgray", width=30)
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(ventana, font=("Consola",11))
entry_nombre.grid(row=0, column=1)

label_precio = tk.Label(ventana, text="Precio: $", font=("Times", 11), bg="lightgray", width=30)
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(ventana, font=("Consola",11))
entry_precio.grid(row=1, column=1)

label_cantidad = tk.Label(ventana, text="Cantidad: ", font=("Times", 11), bg="lightgray", width=30)
label_cantidad.grid(row=2, column=0)
entry_cantidad = tk.Entry(ventana, font=("Consola",11))
entry_cantidad.grid(row=2, column=1)

label_total = tk.Label(ventana, text="$0.0", font=("Consola",12), bg="lightgreen")
label_total.grid(row=4, column=2)

label_error = tk.Label(ventana, text=" ", bg="lightblue")
label_error.grid(row=3,column=0)

texto = tk.Text(ventana, width=30, height=5, wrap="word")
texto.grid(row=4, column=0)

ventana.mainloop()