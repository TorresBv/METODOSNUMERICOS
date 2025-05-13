import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito
V = 10      # Voltios
R = 1000    # Ohmios
C = 0.001   # Faradios

# Definición de la EDO para la carga del capacitor
def dqdt(t, q):
    return (V - q / C) / R

# Método de Runge-Kutta de cuarto orden
def runge_kutta_4(f, t0, q0, t_end, h):
    t_vals = [t0]
    q_vals = [q0]

    t = t0
    q = q0

    while t < t_end:
        k1 = f(t, q)
        k2 = f(t + h/2, q + h/2 * k1)
        k3 = f(t + h/2, q + h/2 * k2)
        k4 = f(t + h, q + h * k3)

        q += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h

        t_vals.append(t)
        q_vals.append(q)

    return t_vals, q_vals

# Condiciones iniciales
t0 = 0       # Tiempo inicial (segundos)
q0 = 0       # Carga inicial (Coulombs)
t_end = 1    # Tiempo final (segundos)
h = 0.05     # Tamaño del paso

# Aplicar el método de Runge-Kutta
t_rk4, q_rk4 = runge_kutta_4(dqdt, t0, q0, t_end, h)

# Graficar la carga q(t)
plt.figure(figsize=(10, 6))
plt.plot(t_rk4, q_rk4, 'bo-', label='Carga q(t) (Runge-Kutta 4)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Carga (C)')
plt.title('Carga de un capacitor en un circuito RC')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("carga_capacitor_rk4.png")
plt.show()

# Imprimir algunos valores de la carga
print("\nValores de la carga q(t):")
for i in range(len(t_rk4)):
    print(f"Tiempo t = {t_rk4[i]:.2f} s, Carga q = {q_rk4[i]:.6f} C")