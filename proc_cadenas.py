
texto = """
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno 
de los estantes (usando 'F' para indicar el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe
ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0).
Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de 
páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.    
"""

contador = 0
i = 0
while i < len(texto):
    # DESCARTAR CARACTERES QUE NO SON LETRAS
    while i < len(texto) and texto[i] == ' ':
        i += 1
    # TRABAJO CON LAS LETRAS DE UNA PALABRA
    palabra = ""
    while i < len(texto) and texto[i] != ' ':
        palabra += texto[i]
        i += 1
    if len(palabra) > 0:
        contador += 1
print(texto)
print(f"La cantidad de palabras es: {contador}")