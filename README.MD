# Manejo de Excepciones en Python

## Descripción

Este repositorio contiene el desarrollo de la actividad **GA1-220501096-01-AA1-EV05 – Python Intermedio: Manejo de Excepciones**, enfocada en el aprendizaje y aplicación del manejo de errores en Python.

En este proyecto se incluyen ejemplos prácticos relacionados con:

- Uso de `try` y `except`
- Manejo de excepciones específicas
- Uso de `else` y `finally`
- Lanzamiento de excepciones con `raise`
- Validación de datos
- Creación de excepciones personalizadas
- Buenas prácticas en el control de errores

Además, se desarrolló un reto práctico donde se implementa una función capaz de capturar errores comunes como `ValueError` y `ZeroDivisionError`, mostrando mensajes personalizados y garantizando la correcta finalización del programa mediante `finally`.

El objetivo principal de esta actividad es comprender la importancia del manejo de excepciones para desarrollar programas más seguros, organizados y resistentes ante errores durante la ejecución.

<details>
<summary> Try-Except </summary>

# Ejemplo 1 — Uso básico de try-except

## Código

```python
try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")

except:
    print("¡Ups! No se puede dividir entre cero.")
```

## Ejecución

```bash
py ejemplos/Try-except/Ejemplo_Sencillo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Try%20(1).png)

---

# Ejemplo 2 — Capturando excepciones específicas

## Código

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"100 dividido por {numero} es {resultado}")

except ZeroDivisionError:
    print("No puedes dividir entre cero.")

except ValueError:
    print("Debes introducir un número válido.")
```

## Ejecución

```bash
py ejemplos/Try-except/Excepciones_Especificas.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Try%20(2).png)

---

# Ejemplo 3 — Accediendo a la información de la excepción

## Código

```python
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()

except FileNotFoundError as error:
    print(f"Error: {error}")
    print("Creando un archivo nuevo...")

    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")
```

## Ejecución

```bash
py ejemplos/Try-except/Accediendo_Informacion_Excepcion.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Try%20(3).png)

---

# Ejemplo 4 — Combinando múltiples excepciones

## Código

```python
try:
    archivo = open("datos.txt", "r")
    valor = int(archivo.readline().strip())
    resultado = 100 / valor

except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error: {type(e).__name__}")
    print(f"Descripción: {e}")
```

## Ejecución

```bash
py ejemplos/Try-except/Combinando_Excepciones.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Try%20(4).png)

---

# Ejemplo 5 — Uso práctico en aplicaciones reales

## Código

```python
def obtener_edad():

    while True:

        try:
            edad = int(input("¿Cuál es tu edad? "))

            if edad < 0:
                print("La edad no puede ser negativa.")
                continue

            return edad

        except ValueError:
            print("Por favor, introduce un número entero.")

edad_usuario = obtener_edad()

print(f"Tu edad es: {edad_usuario}")
```

## Ejecución

```bash
py ejemplos/Try-except/Aplicaciones_Reales.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Try%20(5).png)

---

# Ejemplo 6 — Buenas prácticas

## Código

```python
# =========================
# MAL EJEMPLO
# =========================

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    numeros = [int(x) for x in contenido.split()]
    resultado = sum(numeros) / len(numeros)

    print(f"El promedio es: {resultado}")

    archivo.close()

except:
    print("Ocurrió un error")


# =========================
# BUEN EJEMPLO
# =========================

try:
    archivo = open("datos.txt", "r")

except FileNotFoundError:
    print("El archivo 'datos.txt' no existe")
    exit()


try:
    contenido = archivo.read()
    numeros = [int(x) for x in contenido.split()]

except ValueError:
    print("El archivo contiene datos que no son números")

    archivo.close()
    exit()


try:
    resultado = sum(numeros) / len(numeros)

    print(f"El promedio es: {resultado}")

except ZeroDivisionError:
    print("El archivo está vacío, no se puede calcular el promedio")


archivo.close()
```

## Ejecución

```bash
py ejemplos/Try-except/Buenas_Practicas.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Try%20(6).png)

</details>

<details>
<summary>Tipos Comunes</summary>

# Ejemplo 1 — ZeroDivisionError

## Código

```python
try:
    resultado = 5 / 0
except ZeroDivisionError:
    print("No es posible dividir entre cero")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/ZeroDivisionError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(1).png)

---

# Ejemplo 2 — OverflowError

## Código

```python
try:
    resultado = 10.0 ** 1000000
except OverflowError:
    print("El número es demasiado grande para ser representado")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/OverflowError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(2).png)

---

# Ejemplo 3 — TypeError

## Código

```python
try:
    resultado = "42" + 10
except TypeError:
    print("No se pueden sumar tipos diferentes")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/TypeError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(3).png)
---

# Ejemplo 4 — ValueError

## Código

```python
try:
    numero = int("abc")
except ValueError:
    print("La cadena no representa un número válido")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/ValueError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(4).png)

---

# Ejemplo 5 — IndexError

## Código

```python
try:
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError:
    print("El índice está fuera del rango de la lista")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/IndexError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(5).png)

---

# Ejemplo 6 — KeyError

## Código

```python
try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/KeyError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(6).png)

---

# Ejemplo 7 — FileNotFoundError

## Código

```python
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/FileNotFoundError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(7).png)

---

# Ejemplo 8 — PermissionError

## Código

```python
try:
    with open("/etc/passwd", "w") as archivo:
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/PermissionError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(8).png)

---

# Ejemplo 9 — AttributeError

## Código

```python
try:
    texto = "Hola"
    longitud = texto.size
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/AttributeError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(9).png)

---

# Ejemplo 10 — NameError

## Código

```python
try:
    print(variable_no_definida)
except NameError:
    print("La variable no está definida")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/NameError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(10).png)

---

# Ejemplo 11 — ImportError

## Código

```python
try:
    import biblioteca_inexistente
except ImportError:
    print("No se pudo importar el módulo")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/ImportError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(11).png)

---

# Ejemplo 12 — ModuleNotFoundError

## Código

```python
try:
    import modulo_que_no_existe
except ModuleNotFoundError:
    print("El módulo no existe")
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(12).png)

## Ejecución

```bash
py ejemplos/Tipos_Comunes/ModuleNotFoundError_Ejemplo.py
```

---

# Ejemplo 13 — Jerarquía de excepciones

## Código

```python
try:
    resultado = int("abc") / 0
except Exception as e:
    print(f"Se produjo un error:{type(e).__name__}")
    print(f"Descripción:{e}")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/Jerarquia_Excepciones.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(13).png)

---

# Ejemplo 14 — Identificando el tipo de excepción

## Código

```python
try:
    resultado = eval(input("Introduce una expresión: "))
except Exception as e:
    print(f"Error de tipo:{type(e).__name__}")
    print(f"Descripción:{e}")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/Identificar_Excepcion.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(14).png)

---

# Ejemplo 15 — Excepciones en bibliotecas externas

## Código

```python
import requests

try:
    respuesta = requests.get("https://api.ejemplo.com/datos", timeout=1)
    respuesta.raise_for_status()
except requests.exceptions.ConnectionError:
    print("No se pudo conectar al servidor")
except requests.exceptions.Timeout:
    print("La solicitud excedió el tiempo de espera")
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP:{e}")
```

## Ejecución

```bash
py ejemplos/Tipos_Comunes/Bibliotecas_Externas.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Tipos_Comunes%20(15).png)

</details>

<details>
<summary>Else y Finally</summary>

# Ejemplo 1 — Uso de else

## Código

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"El resultado es:{resultado}")
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Uso_Else.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(1).png)

---

# Ejemplo 2 — Else con archivos

## Código

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido = ""
else:
    print("Archivo leído correctamente.")
    archivo.close()
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Else_Archivos.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(2).png)

---

# Ejemplo 3 — Else en operaciones relacionadas

## Código

```python
try:
    datos = obtener_datos_de_api()
    validar_formato(datos)
except ConexionError:
    print("No se pudo conectar con el servidor.")
except FormatoInvalidoError:
    print("Los datos recibidos tienen un formato incorrecto.")
else:
    resultados = procesar_datos(datos)
    guardar_resultados(resultados)
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Else_Operaciones.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(3).png)

---

# Ejemplo 4 — Uso de finally

## Código

```python
try:
    archivo = open("registro.txt", "w")
    archivo.write("Operación iniciada\n")

    resultado = 10 / int(input("Introduce un número: "))

    archivo.write(f"Resultado:{resultado}\n")

except ZeroDivisionError:
    archivo.write("Error: División por cero\n")

except ValueError:
    archivo.write("Error: Valor no válido\n")

finally:
    archivo.write("Operación finalizada\n")
    archivo.close()
    print("Proceso completado")
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Uso_Finally.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(4).png)

---

# Ejemplo 5 — Finally liberando recursos

## Código

```python
conexion = None

try:
    conexion = conectar_a_base_de_datos()
    datos = conexion.ejecutar_consulta("SELECT * FROM usuarios")
    procesar_datos(datos)

except ConexionError:
    print("Error al conectar con la base de datos")

except ConsultaError:
    print("Error al ejecutar la consulta")

finally:
    if conexion:
        conexion.cerrar()
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Finally_Recursos.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(5).png)

---

# Ejemplo 6 — Restaurar estados con finally

## Código

```python
modo_original = sistema.obtener_modo()

try:
    sistema.cambiar_modo("mantenimiento")
    realizar_actualizacion()

except ActualizacionError:
    print("La actualización falló")

finally:
    sistema.cambiar_modo(modo_original)
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Finally_Restaurar_Estado.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(6).png)

---

# Ejemplo 7 — Registrar finalización

## Código

```python
try:
    registrar_inicio("tarea_diaria")
    ejecutar_tarea_diaria()

except Exception as e:
    registrar_error("tarea_diaria", str(e))

finally:
    registrar_finalizacion("tarea_diaria")
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Registrar_Finalizacion.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(7).png)

---

# Ejemplo 8 — Combinando else y finally

## Código

```python
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
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Else_Finally_Combinado.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(8).png)

---

# Ejemplo 9 — Orden de ejecución

## Código

```python
def demostrar_orden():

    try:
        print("1. Ejecutando bloque try")

    except ZeroDivisionError:
        print("2. Ejecutando bloque except")

    else:
        print("3. Ejecutando bloque else")

    finally:
        print("4. Ejecutando bloque finally")

    print("5. Continuando después del bloque try")

demostrar_orden()
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Orden_Ejecucion.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(9).png)

---

# Ejemplo 10 — Return en try/except/finally

## Código

```python
def dividir(a, b):

    try:
        resultado = a / b
        return resultado

    except ZeroDivisionError:
        print("Error: División por cero")
        return None

    finally:
        print("División finalizada")

print(dividir(10, 2))
print(dividir(10, 0))
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Return_Finally.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(10).png)

---

# Ejemplo 11 — Excepciones en finally

## Código

```python
try:
    1 / 0

except ZeroDivisionError:
    print("Capturada división por cero")

finally:
    print("Bloque finally ejecutado")
```

## Ejecución

```bash
py ejemplos/Else_y_Finally/Excepciones_Finally.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Else_y_Finally%20(11).png)

</details>

<details>
<summary>Lanzar Excepciones</summary>

# Ejemplo 1 — Uso básico de raise

## Código

```python
def dividir(a, b):

    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")

    return a / b

try:
    resultado = dividir(10, 0)

except ZeroDivisionError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Uso_Raise.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(1).png)

# Ejemplo 2 — Validación de parámetros

## Código

```python
def calcular_raiz_cuadrada(numero):

    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")

    return numero ** 0.5

try:
    resultado = calcular_raiz_cuadrada(-9)

except ValueError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Validacion_Parametros.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(2).png)

# Ejemplo 3 — Estados imposibles

## Código

```python
def procesar_respuesta(codigo):

    if codigo == 200:
        return "Datos obtenidos"

    elif codigo == 404:
        return None

    else:
        raise RuntimeError(f"Código de respuesta no manejado:{codigo}")

try:
    procesar_respuesta(500)

except RuntimeError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Estados_Imposibles.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(3).png)

# Ejemplo 4 — Precondiciones no cumplidas

## Código

```python
class Cuenta:

    def __init__(self, saldo, activa):
        self.saldo = saldo
        self.esta_activa = activa

def retirar_dinero(cuenta, cantidad):

    if not cuenta.esta_activa:
        raise ValueError("La cuenta no está activa")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")

    if cantidad > cuenta.saldo:
        raise ValueError("Saldo insuficiente")

    cuenta.saldo -= cantidad

    return cuenta.saldo

cuenta = Cuenta(100, True)

try:
    retirar_dinero(cuenta, 200)

except ValueError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Precondiciones.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(4).png)

# Ejemplo 5 — TypeError y ValueError

## Código

```python
def establecer_edad(edad):

    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")

    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")

    return edad

try:
    establecer_edad("veinte")

except (TypeError, ValueError) as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/TypeError_ValueError.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(5).png)

# Ejemplo 6 — Validación de tipos

## Código

```python
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
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Validacion_Tipos.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(6).png)

# Ejemplo 7 — RuntimeError

## Código

```python
def conectar_a_servidor():

    conexion = False

    if not conexion:
        raise RuntimeError("No hay conexión a Internet")

try:
    conectar_a_servidor()

except RuntimeError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/RuntimeError_Ejemplo.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(7).png)

# Ejemplo 8 — Relanzando excepciones

## Código

```python
def procesar_archivo(ruta):

    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()

    except FileNotFoundError as e:
        print(f"Registrando error:{e}")
        raise

try:
    procesar_archivo("archivo.txt")

except FileNotFoundError:
    print("El archivo no existe")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Relanzar_Excepciones.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(8).png)

# Ejemplo 9 — Excepciones encadenadas

## Código

```python
class ConfigurationError(Exception):
    pass

def obtener_configuracion(archivo):

    try:
        with open(archivo, 'r') as f:
            return f.read()

    except FileNotFoundError as e:
        raise ConfigurationError(
            f"Archivo de configuración no encontrado:{archivo}"
        ) from e

try:
    obtener_configuracion("config.txt")

except ConfigurationError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Excepciones_Encadenadas.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(9).png)

---

# Ejemplo 10 — Excepciones personalizadas

## Código

```python
class SaldoInsuficienteError(Exception):

    def __init__(self, saldo, cantidad):

        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo

        mensaje = (
            f"No hay suficiente saldo. "
            f"Saldo:{saldo}, "
            f"Cantidad solicitada:{cantidad}"
        )

        super().__init__(mensaje)

class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

def retirar(cuenta, cantidad):

    if cantidad > cuenta.saldo:
        raise SaldoInsuficienteError(cuenta.saldo, cantidad)

    cuenta.saldo -= cantidad

    return cuenta.saldo

cuenta = Cuenta(100)

try:
    retirar(cuenta, 500)

except SaldoInsuficienteError as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Excepciones_Personalizadas.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(10).png)

---

# Ejemplo 11 — Buenas prácticas

## Código

```python
import os

ruta = "archivo.txt"

if not os.path.exists(ruta):
    raise FileNotFoundError(
        f"No se encontró el archivo:{ruta}"
    )
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Buenas_Practicas.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(11).png)

---

# Ejemplo 12 — Validación temprana

## Código

```python
def procesar_datos(datos):

    if datos is None:
        raise ValueError("Los datos no pueden ser None")

    if not isinstance(datos, list):
        raise TypeError("Los datos deben ser una lista")

    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía")

    print("Procesando datos...")

try:
    procesar_datos([])

except (ValueError, TypeError) as e:
    print(f"Error:{e}")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Validacion_Temprana.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(12).png)

---

# Ejemplo 13 — Validación de entrada de usuario

## Código

```python
def obtener_edad():

    while True:

        try:
            entrada = input("Introduce tu edad: ")

            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacía")

            edad = int(entrada)

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")

            if edad > 120:
                raise ValueError("La edad parece demasiado alta")

            return edad

        except ValueError as e:

            if str(e).startswith("invalid literal for int"):
                print("Por favor, introduce un número válido")

            else:
                print(f"Error:{e}")

try:
    edad_usuario = obtener_edad()

    print(f"Tu edad es:{edad_usuario}")

except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario")
```

## Ejecución

```bash
py ejemplos/Lanzar_Excepciones/Validacion_Entrada_Usuario.py
```

## Captura de ejecución

![Ejecución del programa](/capturas/Ejem_Lanzar_Excepciones%20(13).png)

</details>