try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()

except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")

    archivo = open("datos.txt", "w")
    archivo.write("Archivo creado automáticamente")

else:
    print(f"Contenido leído:{contenido}")

finally:
    print("Operación de archivo completada.")
    archivo.close()