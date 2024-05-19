# Define una función utilizando def que calcule el factorial de un número dado.

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n
    
print(factorial(7))