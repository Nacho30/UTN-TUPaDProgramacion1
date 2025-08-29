numero_1 = 5 #variable 1
numero_2 = 10 #variable 2
suma = numero_1 + numero_2 # permite a python realizar la suma, al ser de tipado dinamico sabe que al poner un "+ " se debe sumar
resta = numero_2 - numero_1 # permite a python realizar la resta
multiplicacion = numero_1 * numero_2 # permite a python realizar la multiplicacion
division = numero_2 / numero_1 # permite a python realizar la division
print("Suma",suma,"resta",resta,"multiplicacion",multiplicacion,"division",division)
nombre = "NACHO"
precio = 2599.99
descuento = 0.15
precio_final = precio - (precio * descuento)
print("Precio final:", precio_final)
cadena = "Hola mundo"
longitud_cadena = len(cadena) # len sirve para obtener la longitud de una cadena
precio2 = int(1500.75) # aqui se utiliza int para convertir el float a int, en modo de truncamiento
nombre2 = "JUAN"
apellido2 = "PÉREZ"
nombre_completo = nombre2 + " " + apellido2 # concatenacion de cadenas
edad = 25
edad_mas_5 = edad + 5
edad_menos_10 = edad - 10
altura = 1.75
altura_por_4 = altura * 4
altura_dividida_3 = altura / 3
print("Nombre completo:", nombre_completo.lower()) # lower() para convertir a minúsculas
print("Nombre", nombre.capitalize()) # capitalize() para poner la primera letra en mayúscula
