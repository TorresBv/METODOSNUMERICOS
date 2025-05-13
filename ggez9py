import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del sistema
g = 9.81  # m/s^2 (aceleración debido a la gravedad)
m = 2.0   # kg (masa del objeto)
k = 0.5   # kg/s (coeficiente de fricción lineal)

# Condición inicial
v0 = 0  # m/s (velocidad inicial)

# Intervalo de tiempo y número de pasos
t_inicial = 0
t_final = 10
n = 50
h = (t_final - t_inicial) / n

# Inicialización de listas para almacenar resultados
t_vals = np.linspace(t_inicial, t_final, n + 1)
v_euler = [v0]
v_analitica = [(m * g / k) * (1 - np.exp(-(k / m) * t)) for t in t_vals]

# Método de Euler
v = v0
for i in range(n):
    dvdt = g - (k / m) * v
    v = v + h * dvdt
    v_euler.append(v)

# Guardar resultados en archivo CSV
data = {
    "tiempo": t_vals,
    "v_euler": v_euler,
    "v_analitica": v_analitica
}
df = pd.DataFrame(data)
csv_path = "caida_libre_resistencia.csv"
df.to_csv(csv_path, index=False)

# Graficar la solución numérica y analítica
plt.figure(figsize=(10, 6))
plt.plot(t_vals, v_euler, 'o-', label='Solución numérica (Euler)', color='blue')
plt.plot(t_vals, v_analitica, '-', label='Solución analítica', color='red')
plt.title('Caída libre con resistencia del aire')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.legend()
image_path = "caida_libre_resistencia.png"
plt.savefig(image_path)
plt.show()