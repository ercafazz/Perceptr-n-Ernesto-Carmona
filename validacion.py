def ValidarEntrada(entrada):
    while True:
        partes = entrada.strip().split(",")
        
        # Eliminar espacios innecesarios
        partes = [x.strip() for x in partes]

        # Verificar cantidad mínima de valores
        if len(partes) < 2:
            print("⚠️ Debe ingresar al menos un sesgo y un peso (mínimo 2 valores).")
        else:
            try:
                # Verificar que todos los valores sean numéricos
                _ = [float(x) for x in partes]
                return ",".join(partes)  # Retorna el string limpio si todo está bien
            except ValueError:
                print("⚠️ Todos los valores deben ser números válidos (usa punto decimal).")

        # Si llega aquí, hubo un error → pedir de nuevo
        entrada = input("❗ Ingrese nuevamente el vector (ej. -0.6, 0.3, -1.4, 0.9): ")
