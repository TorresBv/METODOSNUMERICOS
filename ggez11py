import numpy as np
import matplotlib.pyplot as plt

# Definición de la EDO para la transferencia de calor
def dTdx(x, T):
    return -0.25 * (T - 25)

# Método de Runge-Kutta de cuarto orden
def runge_kutta_4(f, x0, y0, x_end, h):
    x_vals = [x0]
    y_vals = [y0]

    x = x0
    y = y0

    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)

        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h

        x_vals.append(x)
        y_vals.append(y)

    return x_vals, y_vals

# Parámetros del problema
x0 = 0       # Posición inicial (a lo largo del tubo)
T0 = 100     # Temperatura inicial (°C)
x_end = 2    # Longitud final del tubo considerada (metros)
h = 0.1      # Tamaño del paso

# Aplicar el método de Runge-Kutta
x_rk4, T_rk4 = runge_kutta_4(dTdx, x0, T0, x_end, h)

# Calcular la solución exacta para los mismos puntos x
T_exacta = 25 + 75 * np.exp(-0.25 * np.array(x_rk4))

# Graficar el perfil de temperatura
plt.figure(figsize=(10, 6))
plt.plot(x_rk4, T_rk4, 'bo-', label='Solución numérica (Runge-Kutta 4)')
plt.plot(x_rk4, T_exacta, 'r-', label='Solución exacta')
plt.xlabel('Distancia a lo largo del tubo (metros)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura en un tubo con disipación de calor')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("transferencia_calor_tubo.png")
plt.show()

# Imprimir algunos valores para comparar
print("\nComparación de soluciones:")
print(f"{'x (metros)':<10} {'T_RK4 (°C)':<15} {'T_exacta (°C)':<15} {'Error':<10}")
for i in range(len(x_rk4)):
    error = abs(T_rk4[i] - T_exacta[i])
    print(f"{x_rk4[i]:<10.2f} {T_rk4[i]:<15.4f} {T_exacta[i]:<15.4f} {error:<10.4f}")