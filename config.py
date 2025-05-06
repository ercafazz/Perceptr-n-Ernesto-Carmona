import numpy as np
import numpy as np

def ReadConfig(filename):
    try:
        data = np.loadtxt(filename, delimiter=',')
        if data.ndim != 1:
            raise ValueError("El archivo debe contener una sola línea con sesgo y pesos.")
        return list(data)
    except Exception as e:
        print(f"❌ Error al leer el archivo {filename}: {e}")
        return []
