import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos experimentales
longitud = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])  # Longitud (m)
deflexion = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])  # Deflexión (mm)

# 1. Interpolaciones segmentadas
# Lineal
f_linear = interp1d(longitud, deflexion, kind='linear')
# Cuadrática
f_quadratic = interp1d(longitud, deflexion, kind='quadratic')
# Cúbica
f_cubic = interp1d(longitud, deflexion, kind='cubic')

# Puntos para graficar
x_interp = np.linspace(min(longitud), max(longitud), 500)

# 2. Comparación de métodos
print("Comparación de deflexiones en puntos intermedios:")
print("Longitud | Lineal | Cuadrática | Cúbica")
print("----------------------------------------")
for x in [0.5, 1.5, 2.5, 3.5, 4.5]:
    print(f"{x:5.1f}m | {f_linear(x):6.3f} | {f_quadratic(x):9.3f} | {f_cubic(x):6.3f}")

# 3. Gráfica comparativa
plt.figure(figsize=(12, 7))
plt.plot(longitud, deflexion, 'ko', markersize=8, label='Datos experimentales')
plt.plot(x_interp, f_linear(x_interp), 'b-', linewidth=1.5, label='Interpolación lineal')
plt.plot(x_interp, f_quadratic(x_interp), 'r--', linewidth=1.5, label='Interpolación cuadrática')
plt.plot(x_interp, f_cubic(x_interp), 'g:', linewidth=2, label='Interpolación cúbica')

plt.xlabel('Longitud de la viga (m)', fontsize=12)
plt.ylabel('Deflexión (mm)', fontsize=12)
plt.title('Comparación de Métodos de Interpolación para Deflexión de Viga', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()