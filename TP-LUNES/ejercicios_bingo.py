# Bingo 
# 1. Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse. 
# 2. Mostrá el cartón al jugador en forma de matriz. 
# 3. El programa debe sortear números al azar entre 1 y 50, uno por uno. 
# 4. Cada vez que salga un número: 
#    o Si está en el cartón, reemplazarlo por un 0. 
#    o Si no está, avisar que no aparece. 
#    o Mostrar el cartón actualizado después de cada sorteo. 
# 5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!).

bienvenida = "--------------¡Bienvenida al juego de Bingo!--------------"
print(bienvenida)
import random
numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0, 25, 5)]
while True:
    numero_sorteado = random.randint(1, 51)
    print(numero_sorteado)

    for i in range(5):
        for j in range(5):
            if numero_sorteado == carton[i][j]:
                carton[i][j] = 0
                print("El número está en el cartón.")

    for i in range(5):
        for j in range(5):
            print(f"{carton[i][j]:2}", end=" ")
        print()

    if all(cell == 0 for row in carton for cell in row):
        print("¡Bingo!")
        break

    else:
        print("El número no está en el cartón.")
        continue

