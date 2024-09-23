import numpy as np

# Definir la función a integrar
def f(x):
    return (np.sin(x)**2) * np.exp(x)

# Implementar el método de trapecios
def metodo_trapecios(a, b, n):
    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos en el intervalo
    y = f(x)  # Evaluar la función en los puntos
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])  # Fórmula de trapecios
    return integral

# Intervalo de integración
a = 0
b = 2

# Valores para los subintervalos en cada inciso
subintervalos = [2, 8, 16]

# Calcular y mostrar los resultados para cada caso
for n in subintervalos:
    resultado = metodo_trapecios(a, b, n)
    print(f"Con {n} subintervalos, la aproximación es: {resultado:.6f}")
