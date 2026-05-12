def procesar_respuesta(codigo):

    if codigo == 200:
        return "Datos obtenidos"

    elif codigo == 404:
        return None

    else:
        raise RuntimeError(f"Código de respuesta no manejado:{codigo}")

try:
    procesar_respuesta(500)

except RuntimeError as e:
    print(f"Error:{e}")