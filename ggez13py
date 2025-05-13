import numpy as np
import matplotlib.pyplot as plt

# Definición del sistema de ecuaciones de primer orden
def dYdt(t, Y):
    y1, y2 = Y
    dy1dt = y2
    dy2dt = -2*y2 - 5*y1
    return [dy1dt, dy2dt]

# Método de Runge-Kutta de cuarto orden para sistemas de EDOs
def runge_kutta_4_system(f, t0, Y0, t_end, h):
    t_vals = [t0]
    y1_vals = [Y0[0]]
    y2_vals = [Y0[1]]

    t = t0
    Y = Y0

    while t < t_end:
        k1 = f(t, Y)
        k2 = f(t + h/2, [Y[i] + h/2 * k1[i] for i in range(len(Y))])
        k3 = f(t + h/2, [Y[i] + h/2 * k2[i] for i in range(len(Y))])
        k4 = f(t + h, [Y[i] + h * k3[i] for i in range(len(Y))])

        Y_next = [Y[i] + h * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6 for i in range(len(Y))]
        t += h
        Y = Y_next

        t_vals.append(t)
        y1_vals.append(Y[0])
        y2_vals.append(Y[1])

    return t_vals, y1_vals, y2_vals

# Condiciones iniciales
t0 = 0
Y0 = [1, 0]  # [y1(0), y2(0)] = [posición inicial, velocidad inicial]
t_end = 5
h = 0.1

# Aplicar el método de Runge-Kutta para el sistema
t_vals, y1_vals, y2_vals = runge_kutta_4_system(dYdt, t0, Y0, t_end, h)

# Graficar la trayectoria de la masa (posición vs tiempo)
plt.figure(figsize=(10, 6))
plt.plot(t_vals, y1_vals, 'b-', label='Posición (y1)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Posición')
plt.title('Dinámica de un resorte amortiguado')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("resorte_amortiguado_posicion.png")
plt.show()

# Graficar la velocidad vs tiempo (opcional, pero útil para entender el comportamiento)
plt.figure(figsize=(10, 6))
plt.plot(t_vals, y2_vals, 'r-', label='Velocidad (y2)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad')
plt.title('Velocidad de la masa en el sistema amortiguado')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("resorte_amortiguado_velocidad.png")
plt.show()