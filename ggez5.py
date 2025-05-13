import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
carga = np.array([5, 10, 15, 20, 25])  # Carga (kN)
elongacion = np.array([0.6, 1.2, 1.9, 2.5, 3.1])  # Elongación (mm)

# 1. Ajuste lineal por mínimos cuadrados
n = len(carga)
sum_x = np.sum(carga)
sum_y = np.sum(elongacion)
sum_xy = np.sum(carga * elongacion)
sum_x2 = np.sum(carga**2)

# Cálculo de coeficientes
pendiente = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
intercepto = (sum_y - pendiente * sum_x) / n

# Función de regresión lineal
def recta_regresion(x):
    return pendiente * x + intercepto

# 2. Resultados del ajuste
print("Resultados del ajuste lineal:")
print(f"Ecuación de la recta: y = {pendiente:.4f}x + {intercepto:.4f}")
print(f"Pendiente (b): {pendiente:.4f} mm/kN")
print(f"Intercepto (a): {intercepto:.4f} mm")

# Gráfica de resultados
plt.figure(figsize=(10, 6))
plt.plot(carga, elongacion, 'ro', markersize=8, label='Datos experimentales')
plt.plot(carga, recta_regresion(carga), 'b-', linewidth=2, label=f'Ajuste lineal: y = {pendiente:.3f}x + {intercepto:.3f}')
plt.xlabel('Carga aplicada (kN)', fontsize=12)
plt.ylabel('Elongación (mm)', fontsize=12)
plt.title('Relación Carga-Elongación en Barra de Acero', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()