# Ejercicio 39
# Programa con una función para añadir un elemento a un diccionario.

# Función que añade un elemento a un diccionario
def addElementDict (key, value, dict):
    dict[key] = value
    return dict

# Diccionario
diccionario = {
    "julien": 14,
    "laurent": 31,
}

# Llamada a la función
diccionario = addElementDict("baptiste", 29, diccionario)

# Imprimir diccionario
print(diccionario)