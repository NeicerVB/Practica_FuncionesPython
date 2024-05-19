# Utiliza reduce() para calcular el producto de todos los números en una lista.

from functools import reduce

enteros = [number for number in range(1,10)]

resultado = reduce(lambda acc, val: acc * val, enteros)
print(enteros)
print(f"\n{resultado}")