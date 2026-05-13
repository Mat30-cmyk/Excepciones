# # codigo sin class para correcto funcionamiento del ejemplo

# modo_original = sistema.obtener_modo()

# try:
#     sistema.cambiar_modo("mantenimiento")
#     realizar_actualizacion()

# except ActualizacionError:
#     print("La actualización falló")

# finally:
#     sistema.cambiar_modo(modo_original)

class ActualizacionError(Exception):
    pass


class Sistema:

    def __init__(self):
        self.modo = "normal"

    def obtener_modo(self):
        return self.modo

    def cambiar_modo(self, nuevo_modo):
        self.modo = nuevo_modo
        print(f"Modo cambiado a: {self.modo}")


def realizar_actualizacion():

    print("Realizando actualización...")

    # Simulamos un error
    raise ActualizacionError


sistema = Sistema()

modo_original = sistema.obtener_modo()

try:
    sistema.cambiar_modo("mantenimiento")

    realizar_actualizacion()

except ActualizacionError:
    print("La actualización falló")

finally:
    sistema.cambiar_modo(modo_original)

    print("Sistema restaurado correctamente")