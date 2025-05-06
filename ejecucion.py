import numpy as np
def ejecutar_perceptron(entrada, pesos, sesgo, activacion):
    entrada = np.array(entrada)
    suma = np.dot(entrada, pesos) + sesgo
    return activacion(suma)