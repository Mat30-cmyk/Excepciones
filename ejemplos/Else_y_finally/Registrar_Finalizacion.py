# # codigo sin class para correcto funcionamiento del ejemplo

# try:
#     registrar_inicio("tarea_diaria")
#     ejecutar_tarea_diaria()

# except Exception as e:
#     registrar_error("tarea_diaria", str(e))

# finally:
#     registrar_finalizacion("tarea_diaria")

def registrar_inicio(tarea):
    print(f"Iniciando tarea: {tarea}")


def ejecutar_tarea_diaria():

    print("Ejecutando tarea diaria...")

    # Simulamos un error
    raise Exception("Error durante la ejecución de la tarea")


def registrar_error(tarea, error):
    print(f"Error en {tarea}: {error}")


def registrar_finalizacion(tarea):
    print(f"Finalizando tarea: {tarea}")


try:
    registrar_inicio("tarea_diaria")

    ejecutar_tarea_diaria()

except Exception as e:
    registrar_error("tarea_diaria", str(e))

finally:
    registrar_finalizacion("tarea_diaria")