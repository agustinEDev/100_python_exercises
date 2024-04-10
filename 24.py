# Ejercicio 24
# Programa que devuelve la tabla de multiplicar de un número introducido 
# por el usuario.

# Pedimos al usuario que introduzca un número
num = int(input("Introduce un número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")