# Ejercicio 22
# Programa que recorta los decimales de un número a dos.

# Inicializamos el número
num = 187.632587

# Mostramos el número con dos decimales con format()
print("Número con dos decimales:", "{:.2f}".format(num))

# Mostramos el número con dos decimales con round()
print("Número con dos decimales:", round(num, 2))