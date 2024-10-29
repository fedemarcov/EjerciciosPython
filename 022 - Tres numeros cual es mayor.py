"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))


mayor = n1

if n2 > mayor:
    mayor = n2

if n3 > mayor:
    mayor = n3
    
print("El numero mayor es: ", mayor)

# Otra forma de resolverlo es usando max:

# nt = max(n1, n2, n3)

# print("El numero mas grande es: ", nt)
