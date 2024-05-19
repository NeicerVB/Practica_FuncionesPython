# Utiliza map() para elevar al cuadrado cada número en una lista.

def f_cuadratico(x):
    return x**2

enteros = [number for number in range(1,10)]

result = list(map(f_cuadratico, enteros))

print(result)