"""
Mostrar la suma de cada subsecuencia.

1 4 5 7 8 4 0 4 7 8 5 6 1 9 0 1 1 4 5 7 8 0 -1
"""

mayor_suma_sub = -float('inf')
suma_tot = 0
numero = int(input("Numero: "))
while numero != -1:
    suma_sub = 0
    while numero != 0:
        suma_sub += numero
        suma_tot += numero
        numero = int(input("Numero: "))
    # FIN WHILE
    print(f"La suma de la subsecuencia es: {suma_sub}")
    if suma_sub > mayor_suma_sub:
        mayor_suma_sub = suma_sub
    numero = int(input("Numero: "))
# FIN WHILE
print(f"La suma total es: {suma_tot}")
print(f"La suma sub mayor es: {mayor_suma_sub}")