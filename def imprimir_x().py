def imprimir_x():
    matriz = [[' ' for _ in range(9)] for _ in range(9)]

    for i in range(9):
        matriz[i][i] = '*'  # Establecer asterisco en la diagonal principal
        matriz[i][8 - i] = '*'  # Establecer asterisco en la diagonal secundaria

    for fila in matriz:
        print(' '.join(fila))

imprimir_x()