# import os

# ruta = "archivo.txt"

# if not os.path.exists(ruta):
#     raise FileNotFoundError(
#         f"No se encontró el archivo:{ruta}"
#     )

import os

ruta = "archivo.txt"

try:

    if not os.path.exists(ruta):
        raise FileNotFoundError(
            f"No se encontró el archivo: {ruta}"
        )

    print("Archivo encontrado correctamente")

except FileNotFoundError as e:
    print(f"Error: {e}")