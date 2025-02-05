# Función para calcular los errores entre valores dados
def calcular_errores(x, y, valor_real):
    # Calcula la diferencia entre los valores x y y
    diferencia = x - y
    
    # Calcula el error absoluto, que es la diferencia entre el valor real y la diferencia calculada
    error_abs = abs(valor_real - diferencia)
    
    # Calcula el error relativo, que es el error absoluto dividido entre el valor real
    error_rel = error_abs / abs(valor_real)
    
    # Calcula el error porcentual, multiplicando el error relativo por 100
    error_pct = error_rel * 100
    
    # Imprime los resultados para cada tipo de error
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    
    # Devuelve el error absoluto y el error relativo para su uso posterior
    return error_abs, error_rel

# Lista de tuplas que contienen los valores x, y, y el valor real para probar la función
valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)]

# Bucle para iterar sobre los valores y calcular los errores para cada conjunto de datos
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    # Llama a la función calcular_errores para cada conjunto de valores
    calcular_errores(x, y, real)
