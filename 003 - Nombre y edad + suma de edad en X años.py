#Escribir un programa que solicite al usuario su nombre y su edad, 
#después pida una cantidad de años y muestre por pantalla un mensaje
#que indique cuántos años tendrá la persona después de sumarle a su edad
#la cantidad de años ingresada. El mensaje debe tener el siguiente formato:
#'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edadsumada = int(input("Ingrese cuantos años quiere sumar: "))
suma = edad + edadsumada

print("Hola", nombre, ", dentro de", edadsumada, "años, tendras", suma, "años")