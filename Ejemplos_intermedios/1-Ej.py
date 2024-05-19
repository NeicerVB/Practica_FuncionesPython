# Utiliza map() para convertir una lista de temperaturas en Celsius a Fahrenheit.

def gradosFahrenheit(celsius):
    return celsius*1.8+32

def main():
    celsius = [35,40,45]
    fahrenheit = list(map(gradosFahrenheit, celsius))
    print(fahrenheit)

if __name__ == "__main__":
    main()