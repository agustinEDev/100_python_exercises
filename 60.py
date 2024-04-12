# Ejercicio 60
# Programa con una función que calcule el máximo común divisor con el 
# algoritmo de Euclides

def calculoMCD (a, b):
    assert(a > 0 and b > 0)
    while b != 0:
        a, b = b, a%b
    return a

print(calculoMCD(3,5))
print(calculoMCD(5,15))