# Ejercicio 21
# Programa que suma los valores de un diccionario.

# Inicializamos el diccionario
diccionario = {
    "Manzana": 15,
    "Banana": 8,
    "Fresa": 12,
    "Kiwi": 9,
    "Melocotón": 2,
}

# Sumamos los valores del diccionario
"""Forma 1"""
suma = 0

for clave in diccionario:
    suma += diccionario[clave]

print("La suma de los valores del diccionario es:", suma)

"""Forma 2"""
suma = sum(diccionario.values())
print("La suma de los valores del diccionario es:", suma)
