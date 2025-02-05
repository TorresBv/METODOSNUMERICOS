import numpy as np
import matplotlib.pyplot as plt

# Valor real de pi
pi_real = 3.141592653589793

# Valores de N
N_values = [10, 100, 1000, 10000]

# Función para aproximar pi usando la serie de Leibniz
def calcular_pi_aproximado(N):
    return 4 * sum((-1)**n / (2*n + 1) for n in range(N+1))

# Inicializar listas para almacenar resultados
pi_aproximados = []
errores_absolutos = []
errores_relativos = []
errores_cuadraticos = []

# Calcular aproximaciones y errores
for N in N_values:
    pi_aprox = calcular_pi_aproximado(N)
    error_abs = abs(pi_real - pi_aprox)
    error_rel = error_abs / pi_real
    error_cuad = error_abs**2
    
    pi_aproximados.append(pi_aprox)
    errores_absolutos.append(error_abs)
    errores_relativos.append(error_rel)
    errores_cuadraticos.append(error_cuad)

# Imprimir resultados
print(f"{'N':<10}{'π Aproximado':<15}{'Error Absoluto':<20}{'Error Relativo':<20}{'Error Cuadrático':<20}")
for i in range(len(N_values)):
    print(f"{N_values[i]:<10}{pi_aproximados[i]:<15.10f}{errores_absolutos[i]:<20.10f}{errores_relativos[i]:<20.10f}{errores_cuadraticos[i]:<20.10e}")

# Crear una gráfica para los errores absoluto y relativo
plt.figure(figsize=(12, 6))
plt.plot(N_values, errores_absolutos, label='Error Absoluto', marker='o', color='orange')
plt.plot(N_values, errores_relativos, label='Error Relativo', marker='s', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Número de Términos (N)')
plt.ylabel('Error (escala logarítmica)')
plt.title('Errores Absoluto y Relativo en la Aproximación de π')
plt.legend()
plt.grid(True)
plt.show()