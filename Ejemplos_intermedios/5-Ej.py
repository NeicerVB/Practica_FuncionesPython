# Utiliza filter() para obtener una lista de palabras que comiencen con una letra específica de una lista de palabras.

palabras = [
    "pastel",        # comida
    "pizza",         # comida
    "manzana",       # comida
    "tarta",         # comida
    "cumpleaños",    # cumpleaños
    "regalo",        # cumpleaños
    "fiesta",        # cumpleaños
    "velas",         # cumpleaños
    "ordenador",     # tecnología
    "teléfono",      # tecnología
    "internet",      # tecnología
    "programación",  # tecnología
    "escuela",       # educación
    "examen",        # educación
    "clases",        # educación
    "profesor",      # educación
    "chocolate",     # comida
    "invitaciones",  # cumpleaños
    "software",      # tecnología
    "matemáticas"    # educación
]

inician_con_e = list(filter(lambda palabra: palabra.startswith("e"), palabras))

print(inician_con_e)