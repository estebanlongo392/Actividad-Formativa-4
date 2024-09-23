import numpy as np

# Definir la función a integrar
def f(x):
    return (np.sin(x)**2) * np.exp(x)

# Implementar la Regla de Simpson 1/3
def regla_simpson(a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par para la Regla de Simpson.")
    
    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos en el intervalo
    y = f(x)  # Evaluar la función en los puntos
    
    # Aplicar la fórmula de Simpson 1/3
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])
    return integral

# Intervalo de integración
a = 0
b = 2

# Valores para los subintervalos en cada inciso
subintervalos = [2, 8, 16]

# Calcular y mostrar los resultados para cada caso
for n in subintervalos:
    resultado = regla_simpson(a, b, n)
    print(f"Con {n} subintervalos, la aproximación es: {resultado:.6f}")
