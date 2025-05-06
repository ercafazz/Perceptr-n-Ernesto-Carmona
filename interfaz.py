#ERNESTO CARMONA FAZZOLARI
#SECCIÓN 1. TAREA 1: PERCEPTRONES
#COMPUTACIÓN EMERGENTE

import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import numpy as np
from validacion import ValidarEntrada
from config import ReadConfig
from act import escalon, sigmoide
from ejecucion import ejecutar_perceptron

# Leer configuración globalmente
config = ReadConfig("config.txt")
sesgo = config[0]
pesos = config[1:]

# Crear ventana principal
root = tk.Tk()
root.title("Perceptrón - Entrada y Activación")
root.geometry("400x300")

entrada_tipo = tk.StringVar(value="teclado")
funcion_activacion = tk.StringVar(value="escalon")


def mostrar_resultado(salidas):
    resultado_ventana = tk.Toplevel(root)
    resultado_ventana.title("Resultado")
    texto = ScrolledText(resultado_ventana, width=60, height=15)
    texto.pack(padx=10, pady=10)
    for linea in salidas:
        texto.insert(tk.END, linea + "\n")
    texto.config(state="disabled")


def procesar_teclado():
    entrada_str = entrada_texto.get()
    try:
        entrada_str = ValidarEntrada(entrada_str)
        if entrada_str is None:
            return  # Detener ejecución si hubo error

        entrada_vector = [float(x) for x in entrada_str.split(",")]
        if len(entrada_vector) != len(pesos):
            raise ValueError("Longitud del vector no coincide con los pesos.")
        funcion = escalon if funcion_activacion.get() == "escalon" else sigmoide
        salida = ejecutar_perceptron(entrada_vector, pesos, sesgo, funcion)
        mostrar_resultado([f"Entrada: {entrada_vector}", f"Salida: {salida}"])
    except Exception as e:
        messagebox.showerror("Error", str(e))


def procesar_archivo():
    try:
        with open("vectors.txt", "r") as archivo:
            lineas = archivo.readlines()

        funcion = escalon if funcion_activacion.get() == "escalon" else sigmoide
        salidas = []
        for i, linea in enumerate(lineas):
            try:
                entrada_str = ValidarEntrada(linea)
                entrada_vector = [float(x) for x in entrada_str.split(",")]
                if len(entrada_vector) != len(pesos):
                    raise ValueError(f"Vector en línea {i+1} no tiene la longitud correcta.")
                salida = ejecutar_perceptron(entrada_vector, pesos, sesgo, funcion)
                salidas.append(f"Línea {i+1}: Entrada = {entrada_vector} → Salida = {salida}")
            except Exception as e:
                salidas.append(f"Línea {i+1}: Error - {str(e)}")

        mostrar_resultado(salidas)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo 'vector.txt' no fue encontrado.")


# Widgets
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20, fill="x", expand=True)

# Tipo de entrada
ttk.Label(frame, text="Seleccione el tipo de entrada:").pack(anchor="w")
ttk.Radiobutton(frame, text="Teclado", variable=entrada_tipo, value="teclado").pack(anchor="w")
ttk.Radiobutton(frame, text="Archivo", variable=entrada_tipo, value="archivo").pack(anchor="w")

# Función de activación
ttk.Label(frame, text="\nSeleccione la función de activación:").pack(anchor="w")
ttk.Radiobutton(frame, text="Escalón", variable=funcion_activacion, value="escalon").pack(anchor="w")
ttk.Radiobutton(frame, text="Sigmoide", variable=funcion_activacion, value="sigmoide").pack(anchor="w")

# Entrada desde teclado
entrada_texto = ttk.Entry(frame)
ttk.Label(frame, text="\nVector de entrada (si aplica):").pack(anchor="w")
entrada_texto.pack(fill="x")

# Botón procesar

def procesar():
    if entrada_tipo.get() == "teclado":
        procesar_teclado()
    else:
        procesar_archivo()


boton = ttk.Button(frame, text="Ejecutar Perceptrón", command=procesar)
boton.pack(pady=10)

root.mainloop()