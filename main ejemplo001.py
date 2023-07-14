import random



def el_anio(f):
    return f//10000 # AAAA <== |MMDD

def el_mes(f):
    return (f//100)%100 # AAA| ==> MM <== |DD

def el_dia(f):
    return f%100 # AAAAMM| ==> DD

def str_fecha(f):
    d = el_dia(f)
    m = el_mes(f)
    a = el_anio(f)
    return f"{d:02}/{m:02}/{a:04}"


"""

PROGRAMA PRINCIPAL

"""

def main():
    fecha = int(19910918)
    cadena = str_fecha(fecha)
    print(cadena)


main()   # LLAMO A LA FUNCION PRINCIPAL