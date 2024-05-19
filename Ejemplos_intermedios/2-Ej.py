# Utiliza filter() para obtener una lista de números pares de una lista de números enteros

import random

random.seed(80)
enteros = [random.randint(1,100) for x in range(1,100)]

pares = list(filter(lambda x: x%2 == 0, enteros))

print(enteros)
print(f"\n{pares}")