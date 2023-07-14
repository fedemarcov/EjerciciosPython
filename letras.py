FILAS = 9
COLUMNAS = 9

PFILA = 0
PCOLU = 0
UFILA = FILAS - 1
UCOLU = COLUMNAS - 1
MFILA = FILAS//2
MCOLU = COLUMNAS//2

print("Letra O")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == 0 or f == FILAS - 1  or c == 0 or c == COLUMNAS - 1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print ()

print("Letra L")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == FILAS - 1  or c == 0:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print ()

print("Letra S")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == PFILA or f == UFILA or f == MFILA or (f >= MFILA and c == UCOLU) or (f<= MFILA and c == PCOLU):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print ()

print("Letra T")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == 0 or c == MCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print ()

print("Letra X")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == c:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print ()

print("Letra N")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == c or c == PCOLU or c == UCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print ()