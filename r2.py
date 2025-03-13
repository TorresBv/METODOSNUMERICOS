import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definir el nuevo sistema de ecuaciones
A = np.array([
    [8, 2, -1, 0, 0, 0],
    [3, 15, -2, 1, 0, 0],
    [0, -2, 12, 2, -1, 0],
    [0, 1, -1, 9, -2, 1],
    [0, 0, -2, 3, 14, 1],
    [0, 0, 0, 1, -2, 10]
])

b = np.array([10, 24, -18, 16, -9, 22])

# Solución exacta
sol_exacta = np.linalg.solve(A, b)

# Criterio de paro
tolerancia = 1e-6
max_iter = 100

# Implementación del método de Jacobi
def jacobi(A, b, tol, max_iter):
    n = len(A)
    x = np.zeros(n)  # Aproximación inicial
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    soluciones_iterativas = [x.copy()]
    
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i, i]
        
        # Calcular errores
        error_abs = np.linalg.norm(x_new - sol_exacta, ord=1)
        error_rel = np.linalg.norm(x_new - sol_exacta, ord=1) / np.linalg.norm(sol_exacta, ord=1)
        error_cuad = np.linalg.norm(x_new - sol_exacta, ord=2)
        
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)
        soluciones_iterativas.append(x_new.copy())
        
        # Criterio de convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        
        x = x_new
    
    return x, errores_abs, errores_rel, errores_cuad, k+1, soluciones_iterativas

# Ejecutar el método de Jacobi
sol_aprox, errores_abs, errores_rel, errores_cuad, iteraciones, soluciones_iterativas = jacobi(A, b, tolerancia, max_iter)

# --- Informe ---

# 1. Tablas con las soluciones iterativas
tabla_soluciones = pd.DataFrame(soluciones_iterativas)
tabla_soluciones.index.name = "Iteración"
print("\n1. Tablas con las soluciones iterativas:\n")
print(tabla_soluciones)

# 2. Gráficas de los errores absoluto, relativo y cuadrático
plt.figure(figsize=(8,6))
plt.plot(range(1, iteraciones+1), errores_abs, label="Error absoluto", marker='o')
plt.plot(range(1, iteraciones+1), errores_rel, label="Error relativo", marker='s')
plt.plot(range(1, iteraciones+1), errores_cuad, label="Error cuadrático", marker='d')
plt.xlabel("Iteraciones")
plt.ylabel("Error")
plt.yscale("log")
plt.title("Convergencia de los errores en el método de Jacobi")
plt.legend()
plt.grid()
plt.savefig("errores_jacobi.png")
plt.show()

# 3. Análisis de la convergencia
print("\n3. Análisis de la convergencia:\n")
print(f"El método de Jacobi convergió en {iteraciones} iteraciones.")
print(f"La tolerancia alcanzada fue de {np.linalg.norm(soluciones_iterativas[-1] - sol_exacta, ord=np.inf):.6f}.")

# 4. Comparación con la solución exacta
print("\n4. Comparación con la solución exacta:\n")
print(f"Solución aproximada: {sol_aprox}")
print(f"Solución exacta: {sol_exacta}")
print(f"Error absoluto entre soluciones: {np.linalg.norm(sol_aprox - sol_exacta, ord=1):.6f}")
