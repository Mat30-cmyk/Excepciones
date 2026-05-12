def procesar_datos(datos):

    if datos is None:
        raise ValueError("Los datos no pueden ser None")

    if not isinstance(datos, list):
        raise TypeError("Los datos deben ser una lista")

    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía")

    print("Procesando datos...")

try:
    procesar_datos([])

except (ValueError, TypeError) as e:
    print(f"Error:{e}")