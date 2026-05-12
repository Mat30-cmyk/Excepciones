import os

ruta = "archivo.txt"

if not os.path.exists(ruta):
    raise FileNotFoundError(
        f"No se encontró el archivo:{ruta}"
    )