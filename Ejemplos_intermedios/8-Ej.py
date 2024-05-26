# COMPOSICIÓN DE FUNCIONES
# Escribe una función de orden superior que tome dos funciones f y g y devuelva una nueva función que sea la composición de f y g (es decir, una función que, dada una entrada x, devuelva f(g(x))).

from math import factorial

# 1. Calculamos la operación de combinatoria
def combinatoria(k,n,p):
    return factorial(n) / (factorial(k) * factorial(n-k)), p, k, n

# 2. Calculamos el exito de interés
def exito_fracaso(combinatoria):
    comb, prob, num_success, state = combinatoria
    exito = pow(prob, num_success) * pow(1-prob, state-num_success)
    return comb*exito

# 3. Definimos la función de orden superior para calcular la binomial de
# de un éxito de nuestro interés
def binomial(k,n,p, combinatoria=combinatoria, exito_fracaso=exito_fracaso):
    return exito_fracaso(combinatoria(k,n,p))


print(binomial(3,10,0.4)) # 0.21499084799999987