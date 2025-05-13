import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
T = np.array([200, 250, 300, 350, 400])  # Temperatura de entrada (°C)
eficiencia = np.array([30, 35, 40, 46, 53])  # Eficiencia (%)

# 1. Interpolación de Newton
def interpolacion_newton(x, y):
    n = len(x)
    coeficientes = np.zeros([n, n])
    coeficientes[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coeficientes[i,j] = (coeficientes[i+1, j-1] - coeficientes[i, j-1]) / (x[i+j] - x[i])
    
    return coeficientes[0]

def evaluar_polinomio(coef, x, x_val):
    n = len(coef)
    resultado = coef[0]
    producto = 1
    
    for i in range(1, n):
        producto *= (x_val - x[i-1])
        resultado += coef[i] * producto
    
    return resultado

# Calculamos los coeficientes del polinomio
coeficientes = interpolacion_newton(T, eficiencia)

# Mostramos la ecuación
print("Polinomio de interpolación de Newton:")
print(f"η(T) = {coeficientes[0]:.5f}", end="")
for i in range(1, len(coeficientes)):
    print(f" + {coeficientes[i]:.5f}", end="")
    for j in range(i):
        print(f"(T - {T[j]})", end="")
print("\n")

# 2. Estimación para 275°C
T_estimado = 275
eficiencia_estimada = evaluar_polinomio(coeficientes, T, T_estimado)
print(f"2. La eficiencia estimada para una temperatura de {T_estimado}°C es: {eficiencia_estimada:.2f}%")

# 3. Gráfica de la interpolación
T_interp = np.linspace(min(T), max(T), 100)
eficiencia_interp = [evaluar_polinomio(coeficientes, T, Ti) for Ti in T_interp]

plt.figure(figsize=(10, 6))
plt.plot(T, eficiencia, 'ro', label='Datos experimentales')
plt.plot(T_interp, eficiencia_interp, 'b-', label='Interpolación de Newton')
plt.plot(T_estimado, eficiencia_estimada, 'gs', label=f'Estimación para {T_estimado}°C')
plt.xlabel('Temperatura de entrada (°C)')
plt.ylabel('Eficiencia (%)')
plt.title('Interpolación de Newton para Eficiencia vs Temperatura')
plt.grid(True)
plt.legend()
plt.show()