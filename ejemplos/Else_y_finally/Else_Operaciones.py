# # codigo sin class para correcto funcionamiento del ejemplo

# try:
#     datos = obtener_datos_de_api()
#     validar_formato(datos)
# except ConexionError:
#     print("No se pudo conectar con el servidor.")
# except FormatoInvalidoError:
#     print("Los datos recibidos tienen un formato incorrecto.")
# else:
#     # Solo procesamos si obtuvimos y validamos los datos correctamente
#     resultados = procesar_datos(datos)
#     guardar_resultados(resultados)

class ConexionError(Exception):
    pass

class FormatoInvalidoError(Exception):
    pass


def obtener_datos_de_api():
    # Simulamos datos obtenidos
    return {"nombre": "Teo", "edad": 20}


def validar_formato(datos):

    # Verificamos que exista la clave "nombre"
    if "nombre" not in datos:
        raise FormatoInvalidoError


def procesar_datos(datos):
    return f"Procesando datos de {datos['nombre']}"


def guardar_resultados(resultados):
    print("Resultados guardados:")
    print(resultados)


try:
    datos = obtener_datos_de_api()
    validar_formato(datos)

except ConexionError:
    print("No se pudo conectar con el servidor.")

except FormatoInvalidoError:
    print("Los datos recibidos tienen un formato incorrecto.")

else:
    # Solo se ejecuta si NO hubo excepciones
    resultados = procesar_datos(datos)
    guardar_resultados(resultados)