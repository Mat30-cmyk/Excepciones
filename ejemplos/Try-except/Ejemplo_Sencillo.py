# Bloque try: intenta ejecutar el código
try:
    
    # Se crea la variable numero1 con valor 10
    numero1 = 10
    
    # Se crea la variable numero2 con valor 0
    numero2 = 0
    
    # Se intenta dividir numero1 entre numero2
    resultado = numero1 / numero2
    
    # Muestra el resultado de la división
    print(f"El resultado es:{resultado}")

# Bloque except: se ejecuta si ocurre un error
except:
    
    # Mensaje que aparece porque no se puede dividir entre cero
    print("¡Ups! No se puede dividir entre cero.")