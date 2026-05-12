def conectar_a_servidor():

    conexion = False

    if not conexion:
        raise RuntimeError("No hay conexión a Internet")

try:
    conectar_a_servidor()

except RuntimeError as e:
    print(f"Error:{e}")