"""
Leer 10 numeros desde el teclado.
Mostrar la suma.    
"""
# EJEMPLO RANGE
# for contador in range (10)
# for contador in range(1,11): [0,1,2,3,4,5,6,7,8,9,10)
# for contador in range(1,10): [0,1,2,3,4,5,6,7,8,9)
# for contador in range(1,3): [0,1,2)

suma = 0
for contador in range(10):
    numero = int(input("Numero: "))
    suma += numero
print(f"La suma es: {suma}")