# Ejercicio 37
# Programa que llama a una función que suma los elementos de una lista

# Inicializamos la lista
L = [3, 2, 6, 9, -1, 5]


def calcularSuma (lista):
    suma = 0
    for i in lista:
        suma += int(i)

    return suma

print(calcularSuma(L))