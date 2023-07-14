
import random


def isbisiesto(a):
    es = a%4 == 0 and a%100 != 0 or a%400 == 0
    return es

def obtener_cantidad_dias_del_mes(m,anio):
    cantidad = 31
    if m in (4, 6, 9, 11):
        cantidad = 30
    elif m == 2:
        if isbisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28
    return cantidad
        
        

def obtener_fecha_random(anio):
    m = random.randint(1,12)
    cantidad_dias = obtener_cantidad_dias_del_mes(m,anio)
    d = random.randint(1,cantidad_dias)
    return (anio*10000) + (m*100) + d # AAAAMMDD


def el_anio(aaammdd):
    return aaammdd//10000 # AAAA <== |MMDD

def el_mes(aaammdd):
    return (aaammdd//100)%100 # AAA| ==> MM <== |DD

def el_dia(aaammdd):
    return aaammdd%100 # AAAAMM| ==> DD

def str_fecha(aaammdd):
    d = el_dia(aaammdd)
    m = el_mes(aaammdd)
    a = el_anio(aaammdd)
    return f"{d:02}/{m:02}/{a:04}"


"""

PROGRAMA PRINCIPAL

"""

def main():
    fecha = obtener_fecha_random(2023) # AAAAMMDD
    cadena = str_fecha(fecha)
    print(cadena)


main()   # LLAMO A LA FUNCION PRINCIPAL