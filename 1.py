def calcular_precision_maquina():
    # Inicializamos epsilon en 1.0
    epsilon = 1.0

    # Bucle que sigue dividiendo epsilon hasta que (1.0 + epsilon) ya no sea distinto de 1.0
    while (1.0 + epsilon) != 1.0:
        epsilon /= 2.0  # Dividimos epsilon por 2 en cada iteración

    # En la última iteración, epsilon es tan pequeño que (1.0 + epsilon) es igual a 1.0,
    # por lo que debemos regresar al valor anterior (multiplicándolo por 2).
    epsilon *= 2.0

    # Retornamos la precisión de máquina calculada
    return epsilon

# Llamamos a la función para obtener la precisión de máquina
precision = calcular_precision_maquina()

# Imprimimos el resultado
print(f"La precisión de máquina en este sistema es: {precision}")
