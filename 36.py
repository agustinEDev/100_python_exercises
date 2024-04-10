# Ejercicio 36
# Programa que suma los dígitos de un número introducido

# Inicializamos el resultado a cero
resultado = 0

# Pedimos el número por pantalla
num = input("Introduce un número de más de un dígito: ")

# Sumamos los dígitos de la cifra
for digit in num:
    resultado += int(digit)

print("El resultado es: ", resultado)
