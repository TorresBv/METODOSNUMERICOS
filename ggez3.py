import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos experimentales
distancia = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])  # Distancia (cm)
temperatura = np.array([250, 220, 180, 150, 130, 125])  # Temperatura (°C)

# 1. Interpolaciones segmentadas
# Creación de funciones de interpolación
f_linear = interp1d(distancia, temperatura, kind='linear')
f_quadratic = interp1d(distancia, temperatura, kind='quadratic')
f_cubic = interp1d(distancia, temperatura, kind='cubic')

# Puntos para evaluación
x_interp = np.linspace(min(distancia), max(distancia), 500)

# 2. Comparación de métodos en puntos intermedios
print("Comparación de temperaturas en puntos intermedios:")
print("Distancia | Lineal | Cuadrática | Cúbica")
print("----------------------------------------")
for x in [0.5, 1.5, 2.5, 3.5, 4.5]:
    print(f"{x:5.1f} cm | {f_linear(x):6.1f}°C | {f_quadratic(x):9.1f}°C | {f_cubic(x):6.1f}°C")

# 3. Gráfica comparativa
plt.figure(figsize=(12, 7))
plt.plot(distancia, temperatura, 'ko', markersize=8, label='Datos experimentales')
plt.plot(x_interp, f_linear(x_interp), 'b-', linewidth=1.5, label='Interpolación lineal')
plt.plot(x_interp, f_quadratic(x_interp), 'r--', linewidth=1.5, label='Interpolación cuadrática')
plt.plot(x_interp, f_cubic(x_interp), 'g:', linewidth=2, label='Interpolación cúbic')

plt.xlabel('Distancia desde la cabeza del cilindro (cm)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Distribución de Temperatura en el Cilindro del Motor', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()