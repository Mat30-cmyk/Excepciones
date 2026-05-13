# Bloque try: intenta abrir y leer un archivo
try:
    
    # Intenta abrir el archivo en modo lectura ("r")
    with open("archivo_inexistente.txt", "r") as archivo:
        
        # Lee el contenido del archivo
        contenido = archivo.read()

# Se ejecuta si el archivo no existe
except FileNotFoundError as error:
    
    # Muestra el error generado por Python
    print(f"Error: {error}")
    
    # Mensaje indicando que se creará un nuevo archivo
    print("Creando un archivo nuevo...")
    
    # Crea un archivo nuevo en modo escritura ("w")
    with open("archivo_inexistente.txt", "w") as archivo:
        
        # Escribe texto dentro del nuevo archivo
        archivo.write("Este es un archivo nuevo")