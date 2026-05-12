try:
    texto = "Hola"
    longitud = texto.size
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")