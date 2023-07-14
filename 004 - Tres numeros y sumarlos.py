#Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa
#debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

suma = (numero1 + numero2 + numero3)

print(numero1, "+", numero2, "+", numero3, "=", suma)