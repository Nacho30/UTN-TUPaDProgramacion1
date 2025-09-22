#---------------------------------------EJERCICIO 1 BUCLE FOR---------------------------------------
bienvenida = "----------Bienvenido al mensaje encriptado----------"
print(bienvenida)
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
correme_la_letra= int(input("Hola ingresa cuantas letras quieres correr: "))
for i in range (5):
    mensajes= input(f"Ingrese el mensaje{i+1}: ").upper()
    mensaje_encriptado = ""

    for letra in mensajes:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + correme_la_letra) % 27
            nueva_letra = alfabeto[nuevo_indice]
            mensaje_encriptado += nueva_letra
        else:
            mensaje_encriptado += letra
    print(f"Mensaje encriptado {i+1}: {mensaje_encriptado}") 
#---------------------------------------EJERCICIO 2 BUCLE WHILE----------------------------------
import random

bienvenida2 = "----------Bienvenido al piedra, papel o tijera----------"
print(bienvenida2)

# Opciones posibles
opciones = ["Piedra", "Papel", "Tijera"]

# Marcadores
jugador_gana = 0
computadora_gana = 0

while True:
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    eleccion = input("Escribe el número de tu opción: ")

    if eleccion == "4":
        print("¡Juego terminado!")
        print(f"Marcador final: Jugador {jugador_gana} - Computadora {computadora_gana}")
        break

    if eleccion not in ["1", "2", "3"]:
        print("Opción inválida. Intenta de nuevo.")
        continue

    # Tu jugada
    jugador = opciones[int(eleccion) - 1]
    # Jugada de la computadora
    computadora = random.choice(opciones)
    print(f"Tú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")

    # Comparar jugadas
    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "Piedra" and computadora == "Tijera") or \
         (jugador == "Tijera" and computadora == "Papel") or \
         (jugador == "Papel" and computadora == "Piedra"):
        print("¡Ganaste!")
        jugador_gana += 1
    else:
        print("¡La computadora gana!")
        computadora_gana += 1