# Bloque try: intenta ejecutar el código
try:
    
    # Intenta abrir el archivo "datos.txt" en modo lectura
    archivo = open("datos.txt", "r")
    
    # Lee la primera línea del archivo, elimina espacios y la convierte en entero
    valor = int(archivo.readline().strip())
    
    # Divide 100 entre el valor obtenido del archivo
    resultado = 100 / valor

# Captura errores relacionados con:
# - Archivo no encontrado
# - Valores no válidos
# - División entre cero
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    
    # Muestra el tipo de error ocurrido
    print(f"Ocurrió un error: {type(e).__name__}")
    
    # Muestra la descripción del error
    print(f"Descripción: {e}")