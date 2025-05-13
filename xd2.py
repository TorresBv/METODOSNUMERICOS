import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
profundidad = np.array([1.0, 2.5, 4.0, 5.5])
temperatura = np.array([85, 78, 69, 60])

# Función para el polinomio de Lagrange
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

# a) Estimación de la temperatura a 3.0 cm
x_estimado = 3.0
y_estimado = lagrange_interp(x_estimado, profundidad, temperatura)
print(f"a) La temperatura estimada a {x_estimado} cm es: {y_estimado:.2f} °C")

# b) Representación gráfica
x_vals = np.linspace(1.0, 5.5, 100)  # Rango [1.0, 5.5] con 100 puntos
y_vals = lagrange_interp(x_vals, profundidad, temperatura)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', label='Interpolación de Lagrange')
plt.plot(profundidad, temperatura, 'ro', label='Datos conocidos')
plt.plot(x_estimado, y_estimado, 'gs', label=f'Estimación a {x_estimado} cm: {y_estimado:.2f}°C')
plt.xlabel('Profundidad (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Estimación de Temperatura en un Motor usando Interpolación de Lagrange')
plt.grid(True)
plt.legend()
plt.show()