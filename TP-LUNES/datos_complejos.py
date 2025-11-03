#Un aventurero quiere organizar su mochila con objetos mágicos. Tu tarea será ayudarlo a 
#programar su mochila en Python.
#Parte 1 – Crear la mochila 
#1. El programa debe pedir al usuario cuántos espacios tendrá la mochila (usar una lista 
#de ese tamaño).  Si el usuario ingresa un valor inválido (texto o número negativo/cero), el 
#programa debe mostrar un mensaje de error y volver a pedir el dato.
#Parte 2 – Menú principal 
#El programa debe mostrar un menú con opciones: 
#1. Guardar objeto → El usuario ingresa la posición en la mochila y el nombre del objeto 
#mágico. Si intenta guardar en una posición que no existe, debe manejarse con 
#IndexError. Si no escribe nada (cadena vacía), debe mostrar un mensaje de error. 
# Si ingresa texto donde debía ingresar un número, manejar con ValueError. 
#2. Ver mochila → Muestra el contenido de cada espacio de la mochila (si está vacío, 
#mostrar "--- vacío ---"). 
#3. Salir → Termina el programa mostrando un mensaje de despedida.
bienvenida = "¡Bienvenido a la mochila mágica!"
print(bienvenida)
def crear_mochila():
    while True:
        try:
            tamano = int(input("Ingrese el tamaño de la mochila: "))
            if tamano > 0:
                return [None] * tamano
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
mochila = crear_mochila()
def mostrar_mochila(mochila):
    for i, item in enumerate(mochila):
        if item is None:
            print(f"Posición {i}: --- vacío ---")
        else:
            print(f"Posición {i}: {item}")
def guardar_objeto(mochila):
    try:
        posicion = int(input("Ingrese la posición donde desea guardar el objeto: "))
        if posicion < 0 or posicion >= len(mochila):
            raise IndexError
        objeto = input("Ingrese el nombre del objeto mágico ✨✨: ").strip()
        if objeto == "":
            print("Error: El nombre del objeto no puede estar vacío.☠☠")
        else:
            mochila[posicion] = objeto
            print(f"Objeto '{objeto}' guardado en la posición {posicion}.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para la posición.")
    except IndexError:
        print("Error: La posición ingresada no existe en la mochila.")
def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar objeto")
        print("2. Ver mochila")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")
        if opcion == "1":
            guardar_objeto(mochila)
        elif opcion == "2":
            mostrar_mochila(mochila)
        elif opcion == "3":
            print("¡Gracias por usar la mochila mágica! ¡Hasta luego! 🫂🫂 ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")
menu()
