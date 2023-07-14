"""
Leer numeros hasta que se ingrese un cero.
Mostrar la suma
"""

#ANTES (PARA TODOS)
sumador = 0
numero = int(input("Numero: "))
while numero != 0:
    #DURANTE (PARA CADA DATO)
    
    sumador += numero
    
    numero = int(input("Numero: "))
# DESPUES (TOTALES)
print(f"La suma es: {sumador}")