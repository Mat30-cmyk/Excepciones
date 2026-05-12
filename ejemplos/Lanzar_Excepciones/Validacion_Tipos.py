def concatenar(texto, repeticiones):

    if not isinstance(texto, str):
        raise TypeError("El primer argumento debe ser una cadena de texto")

    if not isinstance(repeticiones, int):
        raise TypeError("El segundo argumento debe ser un número entero")

    return texto * repeticiones

try:
    concatenar("Hola", "3")

except TypeError as e:
    print(f"Error:{e}")