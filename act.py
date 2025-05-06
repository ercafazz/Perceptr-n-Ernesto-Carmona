import numpy as np

def escalon(valor):
    return 1 if valor >= 0 else 0

def sigmoide(valor):
    return 1 / (1 + np.exp(-valor))