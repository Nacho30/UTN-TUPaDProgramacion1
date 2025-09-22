#Una tienda de electrónicos necesita administrar su inventario de productos. 
# Debes implementar un programa que utilice listas paralelas: una lista productos[] para almacenar los nombres 
# de los productos y otra lista stock[] para almacenar la cantidad disponible de cada producto. 
# Ambas listas deben compartir el mismo índice.

bienvenida = ("Bienvenido al sistema de gestion de iinventario")
print(bienvenida) 
productos = ["notebooks","luz led rgb","televisores","monitores","ram","procesadores"]
stock = [2,3,5,7,8,3]

while True:
    menu = ("Elige una de las siguientes opciones dependiendo que es lo que quieras")
    print("1.Ver todos los productos y su stock")
    print("2.Agregar stock a un producto")
    print("3.Agregar un nuevo producto")
    print("0.Salir")
    menu = int(input("Ingrese una opcion (0-3): "))
    if menu == 0 :
        print("Gracias por ingresar al sistema, hasta pronto")
        break
    elif menu == 1:
        print ("Productos y su stock disponible")
        for i in range (len(productos)):
            print(f"{productos[i]}: {stock[i]} stock disponible")
    elif menu == 2:
        producto = (input("Ingrese el nombre del producto: "))
        if producto in productos:
            ind = productos.index(producto)
            nuevo_stock = int(input("Ingrese la cantidad de nuevo stock: "))
            stock[ind] += nuevo_stock
            print(f"Se han agregado {nuevo_stock} stock a {producto}.")
        else:
            print("Producto no encontrado.")
    elif menu == 3:
        nuevo_producto = (input("Ingrese el nuevo producto: "))
        nuevo_stock = int(input("Ingrese la cantidad de stock: "))
        productos.append(nuevo_producto)
        stock.append(nuevo_stock)
        print(f"Se ha agregado el producto {nuevo_producto} con {nuevo_stock} de stock.")
    else:
        print("Opcion no valida, por favor intente de nuevo")
