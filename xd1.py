import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
posicion = np.array([0.5, 1.0, 1.5, 2.0]) # en metros
deformacion = np.array([1.2, 2.3, 3.7, 5.2]) # en milímetros

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Determinar la deformación esperada en x = 1.25 m
x_interp = 1.25
deformacion_interp = lagrange_interpolation(x_interp, posicion, deformacion)
print(f"La deformación esperada en x = {x_interp} m es: {deformacion_interp:.2f} mm")

# b) Graficar la interpolación en el rango [0.5, 2.0] junto con los puntos originales
x_grafica = np.linspace(min(posicion), max(posicion), 100)
y_grafica = [lagrange_interpolation(x, posicion, deformacion) for x in x_grafica]

plt.figure(figsize=(8, 6))
plt.plot(x_grafica, y_grafica, label="Interpolación de Lagrange", color="blue")
plt.scatter(posicion, deformacion, color="red", label="Puntos de medición")
plt.scatter(x_interp, deformacion_interp, color="green", marker='o', s=100, label=f"Interpolación en x={x_interp}")
plt.xlabel("Posición (m)")
plt.ylabel("Deformación (mm)")
plt.title("Predicción de Deformaciones en una Viga mediante Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.savefig("prediccion_deformaciones.png")
plt.show()