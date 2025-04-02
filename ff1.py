import numpy as np
import matplotlib.pyplot as plt

# Función especificada en el ejercicio
def f(x):
    return x**3 - 2*x**2 + x

# Derivada analítica de f(x)
def df_analytical(x):
    return 3*x**2 - 4*x + 1

# Método de diferencias finitas hacia adelante
def forward_diff(f, x, h=0.2):
    return (f(x + h) - f(x)) / h

# Método de diferencias finitas hacia atrás
def backward_diff(f, x, h=0.2):
    return (f(x) - f(x - h)) / h

# Método de diferencias finitas centradas
def central_diff(f, x, h=0.2):
    return (f(x + h) - f(x - h)) / (2 * h)

# Intervalo de evaluación y paso
a = -1.0
b = 2.0
h = 0.2
x_vals = np.arange(a, b + h, h)  # Incluimos b para asegurar el rango completo

# Cálculo de la derivada analítica
df_exact = df_analytical(x_vals)

# Cálculo de las aproximaciones numéricas
df_forward = forward_diff(f, x_vals, h)
df_backward = backward_diff(f, x_vals, h)
df_central = central_diff(f, x_vals, h)

# Cálculo de errores absolutos
error_forward = np.abs(df_forward - df_exact)
error_backward = np.abs(df_backward - df_exact)
error_central = np.abs(df_central - df_exact)

# Graficar la función y sus derivadas
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), '-', label='Función $x^3 - 2x^2 + x$')
plt.plot(x_vals, df_exact, 'k-', label="Derivada analítica $3x^2 - 4x + 1$")
plt.plot(x_vals, df_forward, 'r--', label='Diferencia hacia adelante')
plt.plot(x_vals, df_backward, 'g-.', label='Diferencia hacia atrás')
plt.plot(x_vals, df_central, 'b:', label='Diferencia centrada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Aproximaciones de la derivada de $x^3 - 2x^2 + x$")
plt.grid()
plt.savefig("derivada_polinomio_aproximaciones.png")
plt.show()

# Graficar los errores
plt.figure(figsize=(10, 6))
plt.plot(x_vals, error_forward, 'r--', label='Error Hacia adelante')
plt.plot(x_vals, error_backward, 'g-.', label='Error Hacia atrás')
plt.plot(x_vals, error_central, 'b:', label='Error Centrada')
plt.xlabel('x')
plt.ylabel('Error absoluto')
plt.legend()
plt.title("Errores en la aproximación de la derivada")
plt.grid()
plt.savefig("derivada_polinomio_errores.png")
plt.show()

# Determinar qué método ofrece menor error
metodos = ['Hacia adelante', 'Hacia atrás', 'Centrada']
errores = [error_forward, error_backward, error_central]
errores_promedio = [np.mean(error) for error in errores]
metodo_menor_error = metodos[np.argmin(errores_promedio)]
print(f"El método que ofrece menor error es: {metodo_menor_error}")