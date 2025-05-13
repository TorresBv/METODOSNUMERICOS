import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
F = np.array([50, 100, 150, 200])  # Carga aplicada (N)
epsilon = np.array([0.12, 0.35, 0.65, 1.05])  # Deformación (mm)

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
coeficientes = interpolacion_newton(F, epsilon)

# Mostramos la ecuación
print("Polinomio de interpolación de Newton:")
print(f"ϵ(F) = {coeficientes[0]:.5f}", end="")
for i in range(1, len(coeficientes)):
    print(f" + {coeficientes[i]:.5f}", end="")
    for j in range(i):
        print(f"(F - {F[j]})", end="")
print("\n")

# 2. Estimación para 125 N
F_estimado = 125
epsilon_estimado = evaluar_polinomio(coeficientes, F, F_estimado)
print(f"2. La deformación estimada para una carga de {F_estimado} N es: {epsilon_estimado:.4f} mm")

# 3. Gráfica de la interpolación
F_interp = np.linspace(min(F), max(F), 100)
epsilon_interp = [evaluar_polinomio(coeficientes, F, fi) for fi in F_interp]

plt.figure(figsize=(10, 6))
plt.plot(F, epsilon, 'ro', label='Datos experimentales')
plt.plot(F_interp, epsilon_interp, 'b-', label='Interpolación de Newton')
plt.plot(F_estimado, epsilon_estimado, 'gs', label=f'Estimación para {F_estimado} N')
plt.xlabel('Carga aplicada (N)')
plt.ylabel('Deformación (mm)')
plt.title('Interpolación de Newton para Deformación vs Carga')
plt.grid(True)
plt.legend()
plt.show()