# FILTRADO Y MAPEO DE LISTAS
# Crea una función de orden superior que tome una lista de números y dos funciones: una función de filtrado (para seleccionar solo los números que cumplen una condición) y una función de mapeo (para transformar los números seleccionados). La función debería devolver una nueva lista con los números filtrados y transformados.
import numpy as np

# 1. Definimos la función de orden superior
def filter_and_transform(filter, transform, numbers: list) -> list:
    return transform(filter(numbers))


# 2. Definimos la función de filtrado según las condiciones.
# -> filtrado: solo números divisibles entre 3,5,
def filtering(numbers: list) -> list:
    return [
        num for num in numbers
        if (num%3 == 0) or (num%5 == 0) or (num%7 == 0)
    ]


# 3. Definimos la función de transformado para los números filtrados
# y aplicandole la siguiente formula: 1 / 1 + np.exp(-número)
def transforming(filter_num: list) -> list:
    formula = lambda number: 1/(1 + np.exp(-number))
    return list(map(formula, filter_num))

np.random.seed(100)
numbers = np.random.randint(10,50, 20)

print(numbers)
print(filter_and_transform(filtering, transforming, numbers))