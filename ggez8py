import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del circuito
R = 1000  # Ω
C = 0.001  # F
V_fuente = 5  # V

# Condición inicial
V0 = 0

# Intervalo de tiempo y número de pasos
t_inicial = 0
t_final = 5
n = 20
h = (t_final - t_inicial) / n

# Inicialización de listas para almacenar resultados
t_vals = np.linspace(t_inicial, t_final, n + 1)
V_euler = [V0]
V_analitica = [V_fuente * (1 - np.exp(-t / (R * C))) for t in t_vals]

# Método de Euler
V = V0
for i in range(n):
    dVdt = (1 / (R * C)) * (V_fuente - V)
    V = V + h * dVdt
    V_euler.append(V)

# Guardar resultados en archivo CSV
data = {
    "tiempo": t_vals,
    "V_euler": V_euler,
    "V_analitica": V_analitica
}
df = pd.DataFrame(data)
csv_path = "carga_capacitor.csv"
df.to_csv(csv_path, index=False)

# Graficar la solución numérica y analítica
plt.figure(figsize=(10, 6))
plt.plot(t_vals, V_euler, 'o-', label='Solución numérica (Euler)', color='blue')
plt.plot(t_vals, V_analitica, '-', label='Solución analítica', color='red')
plt.title('Carga de un capacitor en un circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.legend()
image_path = "carga_capacitor.png"
plt.savefig(image_path)
plt.show()