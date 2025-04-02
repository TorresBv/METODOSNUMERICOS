import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) = sin(x)
def f(x):
    return np.sin(x)

# Derivada analítica f'(x) = cos(x)
def df_analytical(x):
    return np.cos(x)

# Métodos de diferencias finitas
def forward_diff(f, x, h=0.1):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h=0.1):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h=0.1):
    return (f(x + h) - f(x - h)) / (2*h)

# Definir el intervalo y paso
a = 0
b = np.pi
h = 0.1
x_vals = np.arange(a, b + h, h)
df_exact = df_analytical(x_vals)

# Calcular aproximaciones numéricas
df_forward = forward_diff(f, x_vals, h)
df_backward = backward_diff(f, x_vals, h)
df_central = central_diff(f, x_vals, h)

# Calcular errores absolutos
error_forward = np.abs(df_forward - df_exact)
error_backward = np.abs(df_backward - df_exact)
error_central = np.abs(df_central - df_exact)

# Graficar la función y las derivadas
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), label='f(x) = sin(x)', linestyle='dotted')
plt.plot(x_vals, df_exact, 'k-', label="Derivada Analítica f'(x) = cos(x)")
plt.plot(x_vals, df_forward, 'r--', label='Diferencias hacia adelante')
plt.plot(x_vals, df_backward, 'g-.', label='Diferencias hacia atrás')
plt.plot(x_vals, df_central, 'b:', label='Diferencias centradas')
plt.xlabel('x')
plt.ylabel('Valor')
plt.legend()
plt.title('Comparación de Métodos de Diferenciación Numérica')
plt.grid()
plt.show()

# Graficar los errores
plt.figure(figsize=(10, 6))
plt.plot(x_vals, error_forward, 'r--', label='Error Hacia adelante')
plt.plot(x_vals, error_backward, 'g-.', label='Error Hacia atrás')
plt.plot(x_vals, error_central, 'b:', label='Error Centrada')
plt.xlabel('x')
plt.ylabel('Error absoluto')
plt.legend()
plt.title('Errores en Diferenciación Numérica')
plt.grid()
plt.show()
