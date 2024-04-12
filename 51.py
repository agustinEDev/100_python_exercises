# Ejercicio 51
# Programa que mediante una función devuelve el factorial de un número entero.

def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n *= i
        return n
    
# Llamamos a la función
num = int(input("Introduce un número entero: "))
print(f"El factorial de {num} es {factorial(num)}")