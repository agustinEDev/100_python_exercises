# Ejercicio 50
# Programa que mediante una función concatena dos diccionarios

def concatDict (d1, d2, d3):
    d1.update(d2)
    d1.update(d3)
    return d1

# Llamamos a la función
print(concatDict({"a":3, "b":6}, {"c":2, "d":-1}, {}))
print(concatDict({"d":[2,9,4.1]}, {"p":[]}, {"j": 'Hola Mundo!'}))