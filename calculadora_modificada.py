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
ventana.geometry("450x150")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="yellowgreen", font=("Courier", 12, "bold"), relief="ridge") 
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(ventana, font=("Arial", 12), relief="groove") 
entry_num1.grid(row=1, column=0)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="yellowgreen", font=("Courier", 12, "bold"), relief="ridge")
label_num2.grid(row=0, column=2)
entry_num2 = tk.Entry(ventana,font=("Arial", 12), relief="groove", bd=2)
entry_num2.grid(row=1, column=2)
 
boton_sumar = tk.Button(ventana, text="Sumar", bg="lightgray", fg="black", font=("Verdana",10) ,command=sumar)
boton_sumar.grid(row=0,column=1)

boton_sumar = tk.Button(ventana, text="Resta",bg="lightgray", fg="black", font=("Verdana",10) ,command=resta)
boton_sumar.grid(row=1,column=1)

boton_sumar = tk.Button(ventana, text="Multiplicar", bg="lightgray", fg="black", font=("Verdana",10),command=multiplicacion)
boton_sumar.grid(row=2,column=1)

boton_sumar = tk.Button(ventana, text="Dividir", bg="lightgray", fg="black", font=("Verdana",10),command=dividir)
boton_sumar.grid(row=3,column=1)
 
ventana.mainloop()