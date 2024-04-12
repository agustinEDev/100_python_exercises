# Ejercicio 49
# Calculamos mediante una función el número de valores contenidos en las listas
# asociadas a las claves de un diccionario.

def numValoresDic (diccionario):
    #Inciamos el contador
    elementos = 0
    for key in diccionario:
        # Sumamos el número de elementos en cada lista
        elementos += len(diccionario[key])
    return elementos

# Llamamos a la función
print(numValoresDic({"a": [1,2,3], "b": [3, 'p'], "c": [8]}))
print(numValoresDic({'Julie': [12, 60.1], 'Fred': [26, 75.6], 'David': []}))