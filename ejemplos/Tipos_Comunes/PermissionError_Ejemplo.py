try:
    with open("/etc/passwd", "w") as archivo:
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")