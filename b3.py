import numpy as np
import matplotlib.pyplot as plt
import csv

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    x_prev = np.copy(x)
    errors = []

    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_prev[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        abs_error = np.linalg.norm(x - x_prev, ord=np.inf)
        rel_error = abs_error / (np.linalg.norm(x, ord=np.inf) + 1e-10)
        quad_error = np.linalg.norm(x - x_prev) ** 2

        errors.append((k, abs_error, rel_error, quad_error))

        if abs_error < tol:
            break

        x_prev = np.copy(x)

    return x, errors

# Matriz de coeficientes A
A = np.array([
    [15, -4, -1, -2, 0, 0, 0, 0, 0, 0],
    [-3, 18, -2, 0, -1, 0, 0, 0, 0, 0],
    [-1, -2, 20, 0, 0, -5, 0, 0, 0, 0],
    [-2, -1, -4, 22, 0, 0, -1, 0, 0, 0],
    [0, -1, -3, -1, 25, 0, 0, -2, 0, 0],
    [0, 0, -2, 0, -1, 28, 0, 0, -1, 0],
    [0, 0, 0, -4, 0, -2, 30, 0, 0, -3],
    [0, 0, 0, 0, -1, 0, -1, 35, -2, 0],
    [0, 0, 0, 0, 0, -2, 0, -3, 40, -1],
    [0, 0, 0, 0, 0, 0, -3, 0, -1, 45]
])

# Vector de términos independientes b
b = np.array([200, 250, 180, 300, 270, 310, 320, 400, 450, 500])

# Llama a la función de Gauss-Seidel
x_sol, errors = gauss_seidel(A, b)

# Guardar errores en CSV
with open("errors_economia_lineal.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Iteración", "Error absoluto", "Error relativo", "Error cuadrático"])
    writer.writerows(errors)
    writer.writerow([])
    writer.writerow(["Solución aproximada"])
    for val in x_sol:
        writer.writerow([val])

# Graficar errores
iterations = [e[0] for e in errors]
abs_errors = [e[1] for e in errors]
rel_errors = [e[2] for e in errors]
quad_errors = [e[3] for e in errors]

plt.figure(figsize=(10, 5))
plt.plot(iterations, abs_errors, label="Error absoluto")
plt.plot(iterations, rel_errors, label="Error relativo")
plt.plot(iterations, quad_errors, label="Error cuadrático")
plt.yscale("log")
plt.xlabel("Iteraciones")
plt.ylabel("Errores")
plt.title("Convergencia del método de Gauss-Seidel para el modelo de economía lineal")
plt.legend()
plt.grid()
plt.savefig("convergencia_gauss_seidel_economia_lineal.png")
plt.show()

print("Solución aproximada:")
print(x_sol)



