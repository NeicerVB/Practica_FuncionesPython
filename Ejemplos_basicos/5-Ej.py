# Define una función utilizando def que reciba una lista de números y retorne la suma de todos ellos.

def sumatorio(values:list) -> int:
    if len(values) == 1:
        return values[-1]
    else:
        return sumatorio(values[:-1]) + values[-1]

print(sumatorio([1,2,3,4]))