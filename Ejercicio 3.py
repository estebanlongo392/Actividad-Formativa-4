import numpy as np

# Definir la función a integrar
def f(x):
    return (np.sin(x)**2) * np.exp(x)

# Implementar la Regla de Simpson 3/8
def regla_simpson_38(a, b, n):
    if n % 3 != 0:
        raise ValueError("El número de subintervalos debe ser múltiplo de 3 para la Regla de Simpson 3/8.")
    
    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos en el intervalo
    y = f(x)  # Evaluar la función en los puntos
    
    # Aplicar la fórmula de Simpson 3/8
    suma_interior = 0
    for i in range(1, n):
        if i % 3 == 0:
            suma_interior += 2 * y[i]
        else:
            suma_interior += 3 * y[i]
    
    integral = (3 * h / 8) * (y[0] + suma_interior + y[n])
    return integral

# Intervalo de integración
a = 0
b = 2

# Valores para los subintervalos en cada inciso (3, 9, 18)
subintervalos = [3, 9, 18]

# Calcular y mostrar los resultados para cada caso
for n in subintervalos:
    resultado = regla_simpson_38(a, b, n)
    print(f"Con {n} subintervalos, la aproximación es: {resultado:.10f}")
