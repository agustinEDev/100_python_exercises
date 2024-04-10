# Ejercicio 34
# Programa que recibe 3 enteros y devuelve el resultado de la función:
# a*(x**3) + 2*a*(x**2) + b

# Pedimos los enteros por pantalla
a = int(input("Introduce el primer número entero: "))
b = int(input("Introduce el segundo número entero: "))
x = int(input("Introduce el tercer número entero: "))

def f(a, b, x):
    print(a*(x**3) + 2*a*(x**2) + b)

f(a, b, x)