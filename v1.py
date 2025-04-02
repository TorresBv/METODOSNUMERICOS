import numpy as np
import matplotlib.pyplot as plt


# Definimos la función a integrar
def f(x):
    return np.exp(-x**2)


# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y


# Parámetros de integración
a, b = 1, 4  # Intervalo de integración
n_values = [5, 10, 15]  # Número de subdivisiones


# Gráficas de aproximación para cada n
plt.figure(figsize=(15, 5 * len(n_values)))  # Ajusta el tamaño de la figura


for i, n in enumerate(n_values):
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)
   
    # Gráfica de la aproximación
    plt.subplot(len(n_values), 1, i + 1)
    x_fine = np.linspace(a, b, 100)
    y_fine = f(x_fine)
    plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = e^{-x^2}$', linewidth=2)
    plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue', label="Aproximación Trapecios")
    plt.plot(x_vals, y_vals, 'bo-', label="Puntos de integración")
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.title(f"Aproximación con n = {n}")
    plt.legend()
    plt.grid()
   
    # Imprimir el resultado de la integral aproximada
    print(f"n = {n}: Integral aproximada = {integral_approx:.6f}")


plt.tight_layout()
plt.show()
