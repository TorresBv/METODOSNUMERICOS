import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
altitud = np.array([2.0, 4.0, 6.0, 8.0])
consumo = np.array([2500, 2300, 2150, 2050])

# Función para el polinomio de Lagrange (la misma del ejercicio anterior)
def lagrange_interp(x, x_points, y_points):
    """
    Interpolación de Lagrange
    x: punto(s) a evaluar
    x_points: puntos x conocidos
    y_points: puntos y conocidos
    """
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Estimación del consumo a 5 km
x_estimado = 5.0
y_estimado = lagrange_interp(x_estimado, altitud, consumo)
print(f"a) El consumo estimado a {x_estimado} km es: {y_estimado:.2f} kg/h")

# b) Representación gráfica
x_vals = np.linspace(2.0, 8.0, 100)  # Rango [2.0, 8.0] con 100 puntos
y_vals = lagrange_interp(x_vals, altitud, consumo)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', label='Interpolación de Lagrange')
plt.plot(altitud, consumo, 'ro', label='Datos conocidos')
plt.plot(x_estimado, y_estimado, 'gs', label=f'Estimación a {x_estimado} km: {y_estimado:.2f} kg/h')
plt.xlabel('Altitud (km)')
plt.ylabel('Consumo de combustible (kg/h)')
plt.title('Predicción del Consumo de Combustible en Aeronaves usando Interpolación de Lagrange')
plt.grid(True)
plt.legend()
plt.show()