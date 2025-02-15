import numpy as np
import matplotlib.pyplot as plt

# Definimos la función g(x) para el método de punto fijo.
def g(x):
    return (3*x - 1)**(1/2)  # Despeje de la ecuación original

# Definimos la derivada de g(x) para analizar la convergencia.
def g_prime(x):
    return (3/2) * (3*x - 1)**(-1/2)

# Funciones para calcular errores
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old)

def error_relativo(x_new, x_old):
    return abs((x_new - x_old) / x_new)

def error_cuadratico(x_new, x_old):
    return (x_new - x_old)**2

# Implementación del método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []  # Lista para guardar los resultados de cada iteración
    errores_abs = []   # Lista para guardar los errores absolutos
    errores_rel = []   # Lista para guardar los errores relativos
    errores_cuad = []  # Lista para guardar los errores cuadráticos

    x_old = x0  # Inicializamos el valor anterior de x con el valor inicial x0
    
    for i in range(max_iter):
        x_new = g(x_old)  # Calculamos el nuevo valor de x aplicando la función g(x)
        e_abs = error_absoluto(x_new, x_old)  # Calculamos el error absoluto
        e_rel = error_relativo(x_new, x_old)  # Calculamos el error relativo
        e_cuad = error_cuadratico(x_new, x_old)  # Calculamos el error cuadrático

        iteraciones.append((i+1, x_new, e_abs, e_rel, e_cuad))  # Guardamos los resultados
        errores_abs.append(e_abs)
        errores_rel.append(e_rel)
        errores_cuad.append(e_cuad)

        if e_abs < tol:  # Verificamos si se alcanza la tolerancia
            break

        x_old = x_new  # Actualizamos el valor anterior de x para la siguiente iteración

    return iteraciones, errores_abs, errores_rel, errores_cuad

# Valor inicial para el método
x0 = 1.5

# Aplicamos el método de punto fijo
iteraciones, errores_abs, errores_rel, errores_cuad = punto_fijo(x0)

# Imprimimos una tabla con los resultados de cada iteración
print("Iteración | x_n       | Error absoluto | Error relativo | Error cuadrático")
print("---------------------------------------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e} | {it[3]:.6e} | {it[4]:.6e}")

# Generamos puntos para graficar la función g(x) y la recta y=x
x_vals = np.linspace(1, 4, 100)  # Ajustamos el rango según la función
y_vals = g(x_vals)

# Graficamos la convergencia del método
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$g(x) = \sqrt{3x - 1}$", color="blue")
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")

# Graficamos las iteraciones
x_points = [it[1] for it in iteraciones]
y_points = [g(x) for x in x_points]
plt.scatter(x_points, y_points, color="black", zorder=3)
plt.plot(x_points, y_points, linestyle="dotted", color="black", label="Iteraciones")

plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.title("Método de Punto Fijo")
plt.savefig("punto_fijo_convergencia.png")
plt.show()

# Graficamos la evolución de los errores
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")
plt.plot(range(1, len(errores_rel) + 1), errores_rel, marker="s", label="Error relativo")
plt.plot(range(1, len(errores_cuad) + 1), errores_cuad, marker="^", label="Error cuadrático")

plt.xlabel("Iteración")
plt.ylabel("Error")
plt.yscale("log")  # Usamos escala logarítmica para mejor visualización
plt.legend()
plt.grid(True)
plt.title("Evolución de los Errores")
plt.savefig("errores_punto_fijo.png")
plt.show()
