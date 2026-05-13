# # codigo sin class para correcto funcionamiento del ejemplo

# conexion = None



# try:
#     conexion = conectar_a_base_de_datos()
#     datos = conexion.ejecutar_consulta("SELECT * FROM usuarios")
#     procesar_datos(datos)
# except ConexionError:
#     print("Error al conectar con la base de datos")
# except ConsultaError:
#     print("Error al ejecutar la consulta")
# finally:
#     if conexion:
#         conexion.cerrar()  # La conexión se cierra siempre

class ConexionError(Exception):
    pass


class ConsultaError(Exception):
    pass


class Conexion:

    def ejecutar_consulta(self, consulta):

        # Simulamos una consulta exitosa
        print(f"Ejecutando consulta: {consulta}")

        return ["Usuario1", "Usuario2", "Usuario3"]

    def cerrar(self):
        print("Conexión cerrada")


def conectar_a_base_de_datos():

    # Simulamos conexión exitosa
    print("Conectando a la base de datos...")

    return Conexion()


def procesar_datos(datos):

    print("Procesando datos...")

    for dato in datos:
        print(dato)


conexion = None

try:
    conexion = conectar_a_base_de_datos()

    datos = conexion.ejecutar_consulta(
        "SELECT * FROM usuarios"
    )

    procesar_datos(datos)

except ConexionError:
    print("Error al conectar con la base de datos")

except ConsultaError:
    print("Error al ejecutar la consulta")

finally:
    if conexion:
        conexion.cerrar()  # La conexión se cierra siempre
