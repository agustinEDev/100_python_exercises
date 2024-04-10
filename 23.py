# Ejercicio 23
# Programa que formatea una cadena de caracteres añadiéndole los valores
# de unas variables.

miNombre, edad, lenguaje = "Agustín", 43, "Python"

# Formateamos la cadena de caracteres
cadena = "Mi nombre es {} y tengo {} años. Me gusta programar en {}."

# Mostramos la cadena de caracteres formateada
print(cadena.format(miNombre, edad, lenguaje))

# Otra forma de formatear la cadena de caracteres
ch = f"Mi nombre es {miNombre} y tengo {edad} años. Me gusta programar en {lenguaje}."
print(ch)