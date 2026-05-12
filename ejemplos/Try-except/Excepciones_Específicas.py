# Bloque try: intenta ejecutar el código
try:
    
    # Solicita al usuario que introduzca un número
    numero = int(input("Introduce un número: "))
    
    # Divide 100 entre el número ingresado
    resultado = 100 / numero
    
    # Muestra el resultado de la división
    print(f"100 dividido por {numero} es {resultado}")

# Se ejecuta si el usuario introduce 0
except ZeroDivisionError:
    
    # Mensaje de error por división entre cero
    print("No puedes dividir entre cero.")

# Se ejecuta si el usuario escribe algo que no sea un número
except ValueError:
    
    # Mensaje de error por dato inválido
    print("Debes introducir un número válido.")