def calcular_recargo(descuento, total):
    return total * descuento / 100

def calcular_iva(total):
    return total * 0.21

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

importe_iva = calcular_iva(total_venta)

# Imprimir los totales
print("***********************************")
print("Forma de Pago           Total")
print("***********************************")
print("Efectivo en Caja        $ {:.2f}".format(efectivo_en_caja))
print("Tarjeta/Crédito         $ {:.2f}".format(tarjeta_credito))
print("Cheques                 $ {:.2f}".format(cheques))
print("Total de Venta          $ {:.2f}".format(total_venta))
print("Importe del IVA         $ {:.2f}".format(importe_iva))