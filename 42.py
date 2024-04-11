# Ejercicio 42
# Programa que imprime medio triángulo de asteriscos.

for numEstrellas in range(1, 11):
    if numEstrellas % 2 == 0 or numEstrellas == 1:
        print("*" * numEstrellas)
        print()