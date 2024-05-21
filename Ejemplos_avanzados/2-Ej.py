# Utiliza una función de orden superior para crear un contador que incremente en una cantidad específica cada vez que se llame

def crear_contador(incremento):
    contador = 0  # Inicializamos el contador en 0

    def incrementar():
        nonlocal contador  # Necesario para modificar la variable de la función externa
        contador += incremento
        return contador
    
    return incrementar

incrementa_2 = crear_contador(2)

print(incrementa_2())
print(incrementa_2())
print(incrementa_2())
print(incrementa_2())