"""Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados
de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.
Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de
los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es
necesario restar la suma de los dos ángulos interiores ingresados al valor 180."

Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?

¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""

num1 = int(input("Ingrese el valor del primer angulo: "))
num2 = int(input("Ingrese el valor del segundo angulo: "))
total = 180

num3 = total - num1 - num2

print("El valor del tercer angulo es: ", num3)
