try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")