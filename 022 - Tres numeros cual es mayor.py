"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

n1 = int(input("Numero1: "))
n2 = int(input("Numero2: "))
n3 = int(input("Numero3: "))

nt = max(n1, n2, n3)

print("El numero mayor es: ", nt)

#Otra forma de resolverlo con logica, en lugar de con "max", es:

n1 = int(input("Numero1: "))
n2 = int(input("Numero2: "))
n3 = int(input("Numero3: "))

mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3

print("Mayor: ", mayor)