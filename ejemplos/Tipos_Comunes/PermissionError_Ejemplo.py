try:
    # este es un archivo de Linux y no funciona en mi pc Windows, por eso lo comento
    # with open("/etc/passwd", "w") as archivo:
    with open("C:/Windows/System32/drivers/etc/hosts", "w") as archivo:
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")