#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
#copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
#utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
#vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
#Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
#elija salir.

bienvenida = ("Bienvenido al sistema de la biblioteca") #Bienvenida
print(bienvenida)
libros = ["el señor de los anillos","it","orgullo y prejuicio"] #lista de libros que hay
stock = [1,3,4] #cantidad de libros en stock

while True:   #Inicializamos el while para mostrar la gama de opciones para el usuario
    menu = ("Bienvenido, elige la opcion que desees")
    print("1.Ingresar titulos")
    print("2.Ingresar ejemplares")
    print("3.Mostrar catalogos")
    print("4.Consultar disponibilidad")
    print("5.Lista de agotados")
    print("6.Agregar titulos")
    print("7.Prestamo/Devolucion")
    print("0.Salir")
    menu = int(input("Elige una opcion : ")) #Usuario ingresa opcion
    if menu == 0:
        print("Hasta pronto ....")
        break
    elif menu == 1:
        print("Los titulos son: ", libros) #Muestra los titulos
    elif menu == 2:
        print("Los ejemplares son: ", stock) #Muestra los ejemplares
    elif menu == 3:
        print("Catalogo: ")
        for i in range(len(libros)):
            print(f"{libros[i]} - Ejemplares: {stock[i]}") #Muestra el catalogo completo
    elif menu == 4:
        print("Ingrese el titulo a consultar")
        titulo = input().lower()
        if titulo in libros:
            print(f"El libro {titulo} tiene {stock[libros.index(titulo)]} ejemplares disponibles")  #Muestra la disponibilidad del libro
        else:
            print("El libro no se encuentra en el catalogo")
    elif menu == 5 :
        print("Libros agotados: ")
        for i in range(len(stock)):
            if stock[i] == 0:
                print(libros[i])  #Muestra los libros que estan agotados
    elif menu == 6: #cuando se le pide ingresar un titulo al usuario se debe de tomar todo en minuscula para evitar errores
        titulo = input("Ingrese el titulo del libro a agregar: ").lower()
        if titulo in libros:
            print("El libro ya existe en el catalogo")
        else:
            libros.append(titulo)
            ejemplares = int(input("Ingrese la cantidad de ejemplares: "))
            stock.append(ejemplares)
            print(f"El libro {titulo} ha sido agregado con {ejemplares} ejemplares")

    elif menu == 7:
        #Opcion donde se le presta al cliente unos de los libros, y se le resta la cantidad de ejemplares que haya en el stock. Caso contrario si el cliente devuelve un libro, incrementa el stock
        titulo = input().lower()
        if titulo in libros:
            while True:
                menu_2= ("Elige una de las opciones dependiendo de lo que quieras hacer")
                print("1.Prestamo")
                print("2.Devolucion")
                menu_2=int(input("Elige una opcion : "))
                if menu_2 == 1 :
                    if stock[libros.index(titulo)] > 0 :
                        stock[libros.index(titulo)] -= 1
                    print(f"El libro {titulo} ha sido prestado con exito")
                    break
                elif menu_2 == 2 :
                    if stock[libros.index(titulo)] > 0 :
                        stock[libros.index(titulo)] += 1
                    print(f"El libro {titulo} ha sido devuelto con exito")
                    break
                else:
                    print(f"El libro {titulo} no tiene ejemplares disponibles")
                    continue
