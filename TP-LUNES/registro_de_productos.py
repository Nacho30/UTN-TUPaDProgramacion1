#Registro de Productos con Archivos CSV 
#Objetivo del trabajo 
#Aplicar los conceptos aprendidos sobre: 
#• Estructuras secuenciales, condicionales y repetitivas. 
#• Funciones y modularización. 
#• Listas y diccionarios. 
#• Manejo de excepciones. 
#• Persistencia de datos mediante archivos CSV. 
#El propósito es crear un pequeño sistema de registro de productos que permita gestionar información de 
#forma sencilla y persistente, utilizando menús y estructuras claras. 
#Consigna general 
#Desarrollá un programa en Python que permita administrar una lista de productos con las siguientes 
#funcionalidades: 
#1. Mostrar todos los productos registrados. 
#o Los datos deben leerse desde un archivo productos.csv. 
#o Si el archivo no existe, debe crearse automáticamente con los encabezados (nombre, 
#precio). 
#o Mostrar cada producto con su nombre y precio, y al final el total acumulado de precios. 
#2. Agregar un nuevo producto. 
#o Pedir al usuario el nombre y el precio. 
#o Validar que el precio sea numérico y positivo. 
#o Guardar el nuevo producto en el archivo sin borrar los anteriores. 
#3. Eliminar un producto existente. 
#o Pedir al usuario el nombre del producto a eliminar. 
#o Si el producto existe, eliminarlo del archivo. 
#o Si no existe, mostrar un mensaje de error. 
#4. Salir del programa. 
#o Finaliza la ejecución del menú. 
#1 
#Programación 1 
#TECNICATURA UNIVERSITARIA 
#EN PROGRAMACIÓN 
#Requisitos técnicos 
#Tu programa debe cumplir con las siguientes condiciones: 
#El menú debe repetirse hasta que el usuario elija la opción “Salir”. 
#El programa debe usar funciones para cada operación (mostrar, agregar, eliminar, etc.). 
#Los productos deben manejarse como diccionarios con claves "nombre" y "precio". 
#El archivo debe manejarse en formato CSV usando el módulo csv de Python. 
#Debés utilizar manejo de excepciones (try / except) para controlar errores de entrada o lectura. 
#No se permite el uso de recursividad. 
#El código debe estar correctamente identado y comentado. 
bienvenido = "Bienvenido al sistema de registro de productos"
menu = """
1. Mostrar todos los productos registrados
2. Agregar un nuevo producto
3. Eliminar un producto existente
4. Salir
"""
import csv
import os

def mostrar_productos():
    """Muestra todos los productos registrados en el archivo CSV."""
    try:
        with open('productos.csv', mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            productos = list(lector)
            if not productos:
                print("No hay productos registrados.")
                return
            total = 0
            print("\nProductos registrados:")
            for producto in productos:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")
                total += float(producto['precio'])
            print(f"Total acumulado de precios: {total}\n")
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo al agregar un producto.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    except ValueError:
        print("Error en el formato de los datos del archivo.")
    except KeyError:
        print("El archivo CSV no tiene las columnas esperadas.")
def agregar_producto():
    """Agrega un nuevo producto al archivo CSV."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    while True:
        try:
            precio = float(input("Ingrese el precio del producto (numérico y positivo): "))
            if precio <= 0:
                raise ValueError("El precio debe ser positivo.")
            break
        except ValueError as ve:
            print(f"Entrada inválida: {ve}. Intente nuevamente.")
    producto = {'nombre': nombre, 'precio': precio}
    try:
        file_exists = os.path.isfile('productos.csv')
        with open('productos.csv', mode='a', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'precio']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            if not file_exists:
                escritor.writeheader()
            escritor.writerow(producto)
        print(f"Producto '{nombre}' agregado exitosamente.\n")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
def eliminar_producto():
    """Elimina un producto existente del archivo CSV."""
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    try:
        with open('productos.csv', mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            productos = list(lector)
        productos_filtrados = [p for p in productos if p['nombre'].lower() != nombre.lower()]
        if len(productos) == len(productos_filtrados):
            print(f"Producto '{nombre}' no encontrado.\n")
            return
        with open('productos.csv', mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'precio']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos_filtrados)
        print(f"Producto '{nombre}' eliminado exitosamente.\n")
    except FileNotFoundError:
        print("El archivo no existe. No hay productos para eliminar.")
    except Exception as e:
        print(f"Error al modificar el archivo: {e}")
def main():
    """Función principal que maneja el menú y las opciones del usuario."""
    print(bienvenido)
    while True:
        print(menu)
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.\n")
if __name__ == "__main__":
    main()
