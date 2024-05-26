# APLICACIÓN DE DESCUENTO
# Define una función de orden superior que tome una lista de precios y una función de descuento (que aplica un descuento específico a un precio) y devuelva una nueva lista con los precios descontados.
import numpy as np

# 1. Lista de precios de caramelos
np.random.seed(40)
Candy_prices = np.random.randint(10,50, 10)

# 2. Crear una función que haga los siguientes descuentos para los caramelos:
# Si está entre 12 y 18 se le hace una descuento del 6%
# Si está entre 25 y 30 se le hace un descuento del 15%
# Para los demás casos se los ignoran y no serán parte de la lista
def discounts(prices: list) -> list:
    dct_six = 0.06
    dct_fifteen = 0.15
    
    """RESOLUCIÓN MIA"""
    # all_products_discounts = list()
    # for price in prices:
    #     if (11 < price) and (21 > price):
    #         all_products_discounts.append(price - (price * dct_six))
    #     elif (24 < price) and (31 > price):
    #         all_products_discounts.append(price - (price * dct_fifteen))
    # return all_products_discounts
    
    """RESOLUCIÓN DE IA"""
    return [
        price - (price * dct_six) if 12 <= price < 18 else
        price - (price * dct_fifteen) if 25 <= price < 30 else
        price
        for price in prices
        if (12 <= price < 18) or (25 <= price < 30)
    ]

def products_with_discounts(rebates, prices: list) -> list:
    return rebates(prices)

print(products_with_discounts(discounts, Candy_prices))