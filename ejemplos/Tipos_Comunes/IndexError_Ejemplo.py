try:
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError:
    print("El índice está fuera del rango de la lista")