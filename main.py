#ERNESTO CARMONA FAZZOLARI
#SECCIÓN 1. TAREA 1: PERCEPTRONES
#COMPUTACIÓN EMERGENTE

import numpy as np
from config import ReadConfig
from act import escalon, sigmoide
from ejecucion import ejecutar_perceptron
from validacion import ValidarEntrada

filename = "config.txt"
configuraciones = ReadConfig(filename)
sesgo = configuraciones[0]
pesos = configuraciones[1:]

while True:

    modo = input("\n¿Entrada por teclado o archivo? (t/a): ").strip().lower()
    while modo not in ["t", "a"]:
        modo = input("Entrada no válida. Por favor, elija 't' para teclado o 'a' para archivo: ").strip().lower()

    funcion = input("Función de activación (escalon (e)/sigmoide (s)): ").strip().lower()
    while funcion not in ["e", "s"]:
        funcion = input("Función no válida. Por favor, elija 'e' para escalon o 's' para sigmoide: ").strip().lower()

    if modo == "t":
        entrada = input("\nIngrese el vector de entrada (separado por comas): ")
        entrada = ValidarEntrada(entrada)
        entrada_vector = [float(x) for x in entrada.split(",")]

        if len(entrada_vector) != len(pesos):
            print(f"❌ Error: El vector de entrada tiene {len(entrada_vector)} componentes, pero se esperaban {len(pesos)}.")
            continue

        activacion = escalon if funcion == "e" else sigmoide
        salida = ejecutar_perceptron(entrada_vector, pesos, sesgo, activacion)
        print("✅ Salida:", salida)

    else:
        try:
            with open("vectors.txt", "r") as archivo:
                lineas = archivo.readlines()

            activacion = escalon if funcion == "e" else sigmoide

            for i, linea in enumerate(lineas):
                entrada = ValidarEntrada(linea)
                entrada_vector = [float(x) for x in entrada.strip().split(",")]

                if len(entrada_vector) != len(pesos):
                    print(f"❌ Vector {i+1}: Error - se esperaban {len(pesos)} componentes, pero se recibieron {len(entrada_vector)}.")
                    continue

                salida = ejecutar_perceptron(entrada_vector, pesos, sesgo, activacion)
                print(f"✅ Vector {i+1}: Entrada = {entrada_vector} → Salida = {salida}")

        except FileNotFoundError:
            print("❌ Error: El archivo 'vector.txt' no fue encontrado.")

    log = input("\n¿DESEA TERMINAR EL PROGRAMA? (s/n): ").strip().lower()
    if log == "s":
        print("✅ PROGRAMA FINALIZADO")
        break
    elif log != "n":
        print("❌ Opción no válida. Por favor, elija 's' para salir o 'n' para continuar.")