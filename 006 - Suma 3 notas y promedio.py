"""Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas
separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.

Ejemplo de ejecución:

Ingrese la nota 1: 7
Ingrese la nota 2: 8
Ingrese la nota 3: 9
Notas: 7, 8, 9
Promedio: 8.0
"""

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1+n2+n3)/3

print(f"Notas: {n1}, {n2}, {n3}")
print("Promedio: ", promedio)