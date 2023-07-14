#Escribir un programa que solicite al usuario ingresar dos notas de un alumno. 
#El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera:
#"Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))

print("Notas:", nota1 , ",", nota2, "==> promedio:", (nota1+nota2)/2)