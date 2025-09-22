#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
edad = int(input(f"Hola {bienvenida}, por favor ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")
else:
    print("Error")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.
bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
nota = float(input(f"Hola {bienvenida}, por favor ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.
bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
numero = int(input(f"Hola {bienvenida}, por favor ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
edad = int(input(f"Hola {bienvenida}, por favor ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
contrasena = input(f"Hola {bienvenida}, por favor ingrese una contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda. 
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda. 
#● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
#6)Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma: import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

import random
import statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Por favor, ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
opcion = int(input(f"Hola {bienvenida}, por favor ingrese el número 1 para transformarlo todo en mayúsculas, el número 2 para transformarlo todo en minúsculas y el número 3 para transformarlo con la primera letra en mayúscula: "))
if opcion == 1:
    print(bienvenida.upper())
elif opcion == 2:
    print(bienvenida.lower())
elif opcion == 3:
    print(bienvenida.title())
else:
    print("Opción no válida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

bienvenida = input("Bienvenido, por favor ingrese su nombre: ")
magnitud = float(input(f"Hola {bienvenida}, por favor ingrese la magnitud del terremoto en numeros enteros<3<4<5<6<7: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# 10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
#Periodo del año                                         / Hemisferio norte       /Hemisferio sur
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)  / Invierno / verano
#Desde el 21 de marzo hasta el 20 de junio (incluidos)  / Primavera / otoño
#Desde el 21 de junio hasta el 20 de septiembre (incluidos)  / Verano / invierno
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)  / Otoño / primavera

bienvenida = input ("Bienvenido, por favor ingrese su nombre: ")
hemisferio = input (f"Hola {bienvenida}, por favor ingrese en cuál hemisferio se encuentra (N/S): ").upper()
mes = int(input (f"Hola {bienvenida}, por favor ingrese el mes en números (1-12): "))
dia = int(input (f"Hola {bienvenida}, por favor ingrese el día en números (1-31): "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
        print("Otoño")
    else:
        print("Fecha no válida")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
        print("Primavera")
    else:
        print("Fecha no válida")
else:
    print("Hemisferio no válido")
