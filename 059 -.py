"""
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:
C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
***********************************
Forma de Pago           Total 
***********************************
Efectivo en Caja        $ xxxx.xx
Tarjeta/Crédito         $ xxxx.xx
Cheques                 $ xxxx.xx
Total de Venta          $ xxxx.xx
"""

def calcular_recargo(descuento, total):
    return total * descuento / 100


# Variables para almacenar los totales
efectivo_en_caja = 0
tarjeta_credito = 0
cheques = 0
total_venta = 0

while True:
    forma_pago = input("Ingrese la forma de pago (C - Cheque, E - Efectivo, T - Tarjeta, F - Finalizar): ").upper()

    if forma_pago == 'F':
        break

    importe_total = float(input("Ingrese el importe total de la venta: "))

    if forma_pago == 'C':
        importe_total += calcular_recargo(20, importe_total)
        cheques += importe_total
    elif forma_pago == 'E':
        importe_total -= calcular_recargo(10, importe_total)
        efectivo_en_caja += importe_total
    elif forma_pago == 'T':
        importe_total += calcular_recargo(12, importe_total)
        tarjeta_credito += importe_total

    total_venta += importe_total

str_totales =f"""
***********************************
Forma de Pago           Total 
***********************************
Efectivo en Caja        $ {efectivo_en_caja}
Tarjeta/Crédito         $ {tarjeta_credito}
Cheques                 $ {cheques}
Total de Venta          $ {total_venta}
""" 

print(str_totales)