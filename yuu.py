import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
V = np.array([10, 20, 30, 40, 50, 60])  # Velocidad del aire (m/s)
Cd = np.array([0.32, 0.30, 0.28, 0.27, 0.26, 0.25])  # Coeficiente de arrastre

# 1. Interpolación de Newton
def newton_interpolation(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i,j] = (coef[i+1, j-1] - coef[i, j-1]) / (x[i+j] - x[i])
    
    return coef[0]

def evaluate_poly(coef, x, x_val):
    n = len(coef)
    result = coef[0]
    product = 1
    
    for i in range(1, n):
        product *= (x_val - x[i-1])
        result += coef[i] * product
    
    return result

# Calculamos los coeficientes
coefficients = newton_interpolation(V, Cd)

# Mostramos la ecuación
print("Polinomio de interpolación de Newton:")
print(f"Cd(V) = {coefficients[0]:.5f}", end="")
for i in range(1, len(coefficients)):
    print(f" + {coefficients[i]:.5f}", end="")
    for j in range(i):
        print(f"(V - {V[j]})", end="")
print("\n")

# 2. Estimación para 35 m/s
V_estimate = 35
Cd_estimate = evaluate_poly(coefficients, V, V_estimate)
print(f"2. El coeficiente de arrastre estimado para V = {V_estimate} m/s es: {Cd_estimate:.4f}")

# 3. Gráfica de la interpolación
V_interp = np.linspace(min(V), max(V), 100)
Cd_interp = [evaluate_poly(coefficients, V, vi) for vi in V_interp]

plt.figure(figsize=(10, 6))
plt.plot(V, Cd, 'ro', markersize=8, label='Datos experimentales')
plt.plot(V_interp, Cd_interp, 'b-', linewidth=2, label='Interpolación de Newton')
plt.plot(V_estimate, Cd_estimate, 'gs', markersize=10, 
         label=f'Estimación para {V_estimate} m/s: {Cd_estimate:.4f}')
plt.xlabel('Velocidad del aire (m/s)', fontsize=12)
plt.ylabel('Coeficiente de arrastre (Cd)', fontsize=12)
plt.title('Interpolación de Newton para Coeficiente de Arrastre vs Velocidad', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()