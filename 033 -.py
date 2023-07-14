"""
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:
Menor de  5500.0 el descuento es del 4.5%  
- ### Entre 5500.0 y  10000.0 el descuento es del 8%  
- ### Más de 10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe:
el descuento y el precio neto a cobrar, con mensajes aclaratorios.
"""

importe = float(input("Importe: "))
if importe < 5550:
    descuento = importe * 4.5/100
elif importe < 10000:
    descuento = importe * 8/100
else:
    descuento = importe * 10.5/100
    
pantalla = f"""
Importe: {importe:10.2f}
Descuento: {descuento:10.2f}
-----------------------------
Importe total: {importe-descuento:10.2f}
"""

print(pantalla)
