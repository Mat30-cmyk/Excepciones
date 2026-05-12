# Función para solicitar y validar la edad del usuario
def obtener_edad():
    
    # Bucle infinito que se repetirá hasta ingresar un dato válido
    while True:
        
        try:
            
            # Solicita al usuario que introduzca su edad
            edad = int(input("¿Cuál es tu edad? "))
            
            # Verifica si la edad es negativa
            if edad < 0:
                
                # Muestra un mensaje de error
                print("La edad no puede ser negativa.")
                
                # Continúa el ciclo para volver a pedir el dato
                continue
            
            # Retorna la edad si es válida
            return edad
        
        # Se ejecuta si el usuario no introduce un número entero
        except ValueError:
            
            # Mensaje de error por dato inválido
            print("Por favor, introduce un número entero.")

# Uso de la función
edad_usuario = obtener_edad()

# Muestra la edad ingresada por el usuario
print(f"Tu edad es: {edad_usuario}")