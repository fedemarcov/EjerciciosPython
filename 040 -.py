"""
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:
a)La suma de los numeros entre a y b
b)La suma de los numeros pares entre a y b.
c)El producto de los numeros impares entre a y b.
"""

a = int(input("Numero a: "))
b = int(input("Numero b: "))

if a > b:
    a,b = b,a

suma = 0
suma_pares = 0
producto_impares = 1

for numero in range(a,b+1):
    suma += numero
    if numero%2 == 0:
        suma_pares += numero
    else:
        producto_impares *= numero
print(f"La suma es: {suma}")
print(f"La suma de los pares es: {suma_pares}")
print(f"El producto de los impares es: {producto_impares}")
