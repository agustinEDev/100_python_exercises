# Ejercicio 20
# Imprime los valores de las claves de un diccionario.

"""Forma 1"""
# Inicializamos el diccionario
diccionario = {
    "Manzana": 3,
    "Banana": 7,
    "Kiwi": 1,
}

# Imprimimos los valores de las claves del diccionario
for clave in diccionario:
    if clave in ("Manzana", "Banana"):
        print("Valor de la clave", clave, ":", diccionario[clave])

"""Forma 2"""
# Inicializamos el diccionario
diccionario = {
    "Manzana": 3,
    "Banana": 7,
    "Kiwi": 1,
}

# Imprimimos los valores de las claves del diccionario
print("Valor de la clave Manzana:", diccionario["Manzana"])
print("Valor de la clave Banana:", diccionario["Banana"])