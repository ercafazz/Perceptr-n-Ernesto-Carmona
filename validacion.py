from tkinter import messagebox

def ValidarEntrada(entrada):
    partes = entrada.strip().split(",")

    # Eliminar espacios
    partes = [x.strip() for x in partes]

    # Validar longitud mínima
    if len(partes) < 2:
        messagebox.showerror("Error", "⚠️ Debe ingresar al menos un sesgo y un peso (mínimo 2 valores).")
        return None

    try:
        _ = [float(x) for x in partes]
        return ",".join(partes)  # Devuelve string limpio
    except ValueError:
        messagebox.showerror("Error", "⚠️ Todos los valores deben ser numéricos (usa punto decimal).")
        return None