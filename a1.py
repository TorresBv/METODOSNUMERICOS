import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**3 - 4*x - 9

# Método de bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None

    iteraciones = []
    errores = []
    c_old = a

    print("\nIteraciones del Método de Bisección:")
    print("Iter |    a        |    b        |    c        |    f(c)       |    Error    ")
    print("-" * 85)

    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)

        error = abs(c - c_old)
        errores.append(error)

        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error:.8e}")

        if abs(f(c)) < tol or error < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return iteraciones, errores

# Parámetros iniciales (intervalo [2, 3] y tolerancia 10^-5)
a, b = 2, 3
tolerancia = 10**-5
iteraciones, errores = biseccion(a, b, tol=tolerancia)

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

ax[0].plot(x, y, label=r'$f(x) = x^3 - 4x - 9$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de convergencia del error
ax[1].plot(range(1, len(errores)+1), errores, marker='o', linestyle='-', color='r')
ax[1].set_yscale("log")
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Error Absoluto")
ax[1].set_title("Error Absoluto en cada Iteración")
ax[1].grid()

# Guardar la figura
plt.savefig("biseccion_convergencia.png", dpi=300)
plt.show()