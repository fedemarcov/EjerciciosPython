"""
Leer numeros hasta que se ingrese un cero.
Mostrar la suma
"""

import random

sumador = 0
contador = 0
numero = random.randint(0,1000)
while numero != 0:
    
    sumador += numero
    contador += 1
    numero = random.randint(0,1000)

print(f"La suma es: {sumador}")
print(f"La cantidad de numeros sumados es: {contador}") 