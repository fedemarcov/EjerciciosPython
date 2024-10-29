"""Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.
"""

persona1 = input("Ingrese el nombre del primer socio: ")
inversion_persona1 = float(input("Ingrese la cantidad invertida por el socio 1: "))
persona2 = input("Ingrese el nombre del segundo socio: ")
inversion_persona2 = float(input("Ingrese la cantidad invertida por el socio 2: "))
persona3 = input("Ingrese el nombre del tercer socio: ")
inversion_persona3 = float(input("Ingrese la cantidad invertida por el socio 3: "))

total = inversion_persona1 + inversion_persona2 + inversion_persona3

porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)
porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)
porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2)

print(f"A {persona1} le pertenece el {porcentaje_inversion_persona1}% de la sociedad")
print(f"A {persona2} le pertenece el {porcentaje_inversion_persona2}% de la sociedad")
print(f"A {persona3} le pertenece el {porcentaje_inversion_persona3}% de la sociedad")