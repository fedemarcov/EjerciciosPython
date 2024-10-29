"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero
es mayor, menor o igual al segundo.
"""

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

if n1 > n2:
    print("Mayor: ", n1)
else:
    if n2 > n1:
        print("Mayor: ", n2)
    else:
        print("Los numeros son iguales.")