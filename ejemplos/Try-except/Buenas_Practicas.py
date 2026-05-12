# =========================
# MAL EJEMPLO
# =========================

# Bloque try demasiado grande
try:
    
    # Abre el archivo "datos.txt" en modo lectura
    archivo = open("datos.txt", "r")
    
    # Lee todo el contenido del archivo
    contenido = archivo.read()
    
    # Convierte los datos del archivo en números enteros
    numeros = [int(x) for x in contenido.split()]
    
    # Calcula el promedio de los números
    resultado = sum(numeros) / len(numeros)
    
    # Muestra el resultado del promedio
    print(f"El promedio es: {resultado}")
    
    # Cierra el archivo
    archivo.close()

# Captura cualquier tipo de error
except:
    
    # Mensaje poco específico del error
    print("Ocurrió un error")


# =========================
# BUEN EJEMPLO
# =========================

# Intenta abrir el archivo
try:
    
    # Abre el archivo en modo lectura
    archivo = open("datos.txt", "r")

# Se ejecuta si el archivo no existe
except FileNotFoundError:
    
    # Mensaje indicando que el archivo no fue encontrado
    print("El archivo 'datos.txt' no existe")
    
    # Finaliza el programa
    exit()


# Intenta leer y convertir los datos del archivo
try:
    
    # Lee el contenido del archivo
    contenido = archivo.read()
    
    # Convierte los datos en números enteros
    numeros = [int(x) for x in contenido.split()]

# Se ejecuta si algún dato no es numérico
except ValueError:
    
    # Mensaje de error por datos inválidos
    print("El archivo contiene datos que no son números")
    
    # Cierra el archivo
    archivo.close()
    
    # Finaliza el programa
    exit()


# Intenta calcular el promedio
try:
    
    # Calcula el promedio de los números
    resultado = sum(numeros) / len(numeros)
    
    # Muestra el promedio calculado
    print(f"El promedio es: {resultado}")

# Se ejecuta si la lista está vacía
except ZeroDivisionError:
    
    # Mensaje indicando que no hay datos para calcular
    print("El archivo está vacío, no se puede calcular el promedio")


# Cierra el archivo al finalizar
archivo.close()