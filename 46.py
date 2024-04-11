# Ejercicio 46
# Función que devuelve los divisores de un número entero en orden ascendente

# Función que devuelve los divisores de un número entero en orden ascendente
def divisores(num):
    Lista = []
    for i in range(1, num+1):
        if num%i == 0:
            Lista.append(i)
    return Lista

# Prueba de la función
print(f"Los divisores de 3 son: {divisores(3)}")
print(f"Los divisores de 9 son : {divisores(9)}")