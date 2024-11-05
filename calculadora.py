import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def resta():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicacion():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multi = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicación es: {multi}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        div = num1 / num2
        messagebox.showinfo("Resultado", f"La divición es: {div}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Esa mamada no se puede")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x400")
 
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=10)

boton_sumar = tk.Button(ventana, text="Resta", command=resta)
boton_sumar.pack(pady=5)

boton_sumar = tk.Button(ventana, text="Multiplicar", command=multiplicacion)
boton_sumar.pack(pady=5)

boton_sumar = tk.Button(ventana, text="Dividir", command=dividir)
boton_sumar.pack(pady=5)
 
ventana.mainloop()