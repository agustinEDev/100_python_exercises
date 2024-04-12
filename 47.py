# Ejercicio 47
# Programa que recibe una cadena y nos dice si hay alguna letra mayúscula

# Función que recibe una cadena y nos dice si hay alguna letra mayúscula
def mayuscula(cadena):
    for letra in cadena:
        if letra.isupper():
            return True
    return False

# Pedimos una cadena por pantalla
cadena = input("Introduce una cadena: ")

# Llamamos a la función y mostramos el resultado
if mayuscula(cadena):
    print("Hay mayúsculas")
else:
    print("No hay mayúsculas")