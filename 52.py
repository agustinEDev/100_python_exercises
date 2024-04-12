# Ejercicio 52
# Programa que mediante una función que recibe un número n, un número a y un 
# umbral, devuelva los números desde cero al umbral que son divisibles por a y 
# no son múltiplos de n.

def divisoresMult (n, a, numUmbral):
    res = []
    for i in range(numUmbral+1):
        if i % n == 0 and i % a != 0:
            res.append(i)
    return res

# Llamamos a la función
num = int(input("Introduce un número entero: "))
num2 = int(input("Introduce otro número entero: "))
umbral = int(input("Introduce un umbral: "))
resultado = divisoresMult(num, num2, umbral)
print("Los números divisibles por", num, "y no múltiplos de", 
      num2, "son:", resultado)
