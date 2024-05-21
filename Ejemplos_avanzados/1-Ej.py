# Define una función que devuelva otra función que eleve al cuadrado un número.

# Aplicamos HIGHER ORDER FUNCTION
# -- recibe almenos un parámetro que sea una función
# -- siempre retorna una función

def cuadratica(number):
    return number**2

def f_activacion(func, value):
    return func(value)


print(f_activacion(cuadratica, 5))