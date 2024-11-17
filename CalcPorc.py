import tkinter as tk
from tkinter import messagebox

def calcular_porcentaje():
    try:
        porc = float(entry_porcentaje.get())
        num = float(entry_numero.get())
        result = porc * num / 100
        messagebox.showinfo("Resultado", f"El {porc}% de {num} es {round(result, 2)}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Porcentaje")
ventana.geometry("300x200")

# Etiqueta y campo para el porcentaje
label_porcentaje = tk.Label(ventana, text="Ingrese el % que desea calcular:")
label_porcentaje.pack(pady=5)
entry_porcentaje = tk.Entry(ventana)
entry_porcentaje.pack(pady=5)

# Etiqueta y campo para el número
label_numero = tk.Label(ventana, text="Ingrese el número a calcular:")
label_numero.pack(pady=5)
entry_numero = tk.Entry(ventana)
entry_numero.pack(pady=5)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_porcentaje)
boton_calcular.pack(pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
