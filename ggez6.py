import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
x = np.array([0, 2, 4, 6, 8])  # Posición (cm)
y = np.array([100, 92, 85, 78, 71])  # Temperatura (°C)

# Ajuste lineal por mínimos cuadrados
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Cálculo de pendiente (m) e intercepto (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

# Función de regresión lineal
def modelo_lineal(x):
    return m * x + b

# Estimación en x = 5 cm
x_estimado = 5
y_estimado = modelo_lineal(x_estimado)

# Resultados
print(f"Modelo lineal: T(x) = {m:.3f}x + {b:.3f}")
print(f"Temperatura estimada en x = 5 cm: {y_estimado:.1f} °C")

# Gráfica
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Datos experimentales')
plt.plot(x, modelo_lineal(x), color='blue', label=f'Regresión: T(x) = {m:.2f}x + {b:.2f}')
plt.scatter(x_estimado, y_estimado, color='green', marker='s', label=f'Estimación en x=5 cm: {y_estimado:.1f} °C')
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Distribución de Temperatura en una Barra')
plt.grid(linestyle='--', alpha=0.6)
plt.legend()
plt.show()