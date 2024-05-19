# Escribe una función recursiva en Python que determine si una palabra es un palíndromo. Un palíndromo es una palabra o frase que se lee igual hacia adelante y hacia atrás, ignorando los espacios, la puntuación y la capitalización.


def palindromo(text, comienzo=0, final=-1):
    result = False
    if comienzo < len(text)-1 :
        if text[comienzo] == text[final]:
            palindromo(text[comienzo+1: final-1])
            result = True
        else:
            result = False
    
    return "El texto es palindromo" if result == True else "El texto no es palindromo"



def es_palindromo(s):
    s = ''.join(c for c in s if c.isalnum())  # Elimina espacios, puntuación y convierte a minúsculas
    if len(s) < 2:  # Si la longitud de s es menor a 2, es un palíndromo
        return "El texto es palindromo"
    elif s[0] != s[-1]:  # Si el primer y último carácter no son iguales, no es un palíndromo
        return "El texto no es palindromo"
    else:
        return es_palindromo(s[1:-1])  # Llamada recursiva al subconjunto de s

# Prueba

text = "reconocer".lower()
print(palindromo(text))
print(es_palindromo(text))
