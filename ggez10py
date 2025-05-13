import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del problema
T_inicial = 90  # °C (temperatura inicial del cuerpo)
T_ambiente = 25  # °C (temperatura ambiente)
k = 0.07        # 1/min (constante de enfriamiento)

# Condición inicial
t0 = 0
T0 = T_inicial

# Intervalo de tiempo y número de pasos
t_inicial_sim = 0
t_final_sim = 30
n = 30
h = (t_final_sim - t_inicial_sim) / n

# Inicialización de listas para almacenar resultados
t_vals = np.linspace(t_inicial_sim, t_final_sim, n + 1)
T_euler = [T0]
T_analitica = [T_ambiente + (T_inicial - T_ambiente) * np.exp(-k * t) for t in t_vals]

# Método de Euler
T = T0
for i in range(n):
    dTdt = -k * (T - T_ambiente)
    T = T + h * dTdt
    T_euler.append(T)

# Guardar resultados en archivo CSV
data = {
    "tiempo": t_vals,
    "T_euler": T_euler,
    "T_analitica": T_analitica
}
df = pd.DataFrame(data)
csv_path = "enfriamiento_newton.csv"
df.to_csv(csv_path, index=False)

# Graficar la solución numérica y analítica
plt.figure(figsize=(10, 6))
plt.plot(t_vals, T_euler, 'o-', label='Solución numérica (Euler)', color='blue')
plt.plot(t_vals, T_analitica, '-', label='Solución analítica', color='red')
plt.title('Ley de Enfriamiento de Newton')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()
image_path = "enfriamiento_newton.png"
plt.savefig(image_path)
plt.show()