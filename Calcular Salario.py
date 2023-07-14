#Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas
# rabajadas por día, para calcular el salario semanal de un trabajador que trabaja todos los días hábiles 
#y la mitad de las horas del día hábil los sábados, suponiendo que todas las horas tienen el mismo valor."

#Como pensarlo:
#1- Pedir al usuario que ingrese el valor monetario de una hora de trabajo y almacenarlo en una variable valor_hora.

#2- Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla en una 
#variable horas_trabajadas_por_dia.

#3- Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia.

#4- Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles
#de la semana. Para esto, puedes utilizar la constante dias_habiles definida como 5.

#5- Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de horas
#trabajadas por día hábil. Para esto, se puede utilizar la vaiable horas_sabado definida como horas_trabajadas_por_dia / 2.

#6- Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por horas_sabado.

#7- Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador.

#8- Mostrar el resultado del salario semanal en la pantalla.

valor_hora = float(input("Valor hora de trabajo: "))
horas_trabajadas_por_dia = float(input("Horas trabajadas por dia: "))
salariodiario = (valor_hora*horas_trabajadas_por_dia)
print("Su salario diario es: ", salariodiario)
salariosemanal = (salariodiario*5.5)
print("Su salario semanal es: ", salariosemanal)
salariomensual = (salariosemanal*4)
print("Su salario mensual es: ", salariomensual)
