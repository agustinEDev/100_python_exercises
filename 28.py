# Ejercicio 28
# Programa que muestra el tiempo de ejecución de un programa.

import time

# Guardamos el tiempo de inicio
start_time = time.time()

# Pedimos por pantalla un número para mostrar su tabla de multiplicar
numero = int(input("Introduce un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")

# Guardamos el tiempo de finalización
end_time = time.time()

# Mostramos el tiempo de ejecución
print(f"El tiempo de ejecución ha sido de {end_time - start_time} segundos.")