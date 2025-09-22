
# RESPETAR TILDES Y PUNTOS FINALES

#Ejercicio 1
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print ('Ejercicio 1')

for num in range(101):
    print(num)

print('')

#Ejercicio 2
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
print ('Ejercicio 2')

user_num = int(input('Ingrese un número entero: '))


n = abs(user_num) # se convierte en positivo

if n == 0:
    digits = 1
else:
    digits = 0
    while n > 0:
        n //= 10   # se quita el ultimo digito
        digits += 1

print(f'Tu número, "{user_num}" tiene {digits} dígito/s.')



print('')

#Ejercicio 3 
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
print ('Ejercicio 3')

num_a = int(input('Ingrese el primer número: '))
num_b = int(input('Ingrese el segundo número: '))


if num_a > num_b:
    num_a, num_b = num_b, num_a # num_a sea menor para que funcione la logica

counter = num_a + 1  # número siguiente a num_a
result = 0

while counter < num_b:  # mientras no lleguemos a num_b (num anterior)
    result += counter
    counter += 1 # 
    # print(result) (1 y 4) = (2+3) = 5

print(f'La suma entre los numeros comprendidos {num_a} y {num_b} es: {result}')


print('')

#Ejercicio 4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
print ('Ejercicio 4')
total = 0

while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    
    if numero == 0:
        break  
    
    total += numero
    
    print(f"Total acumulado: {total}")

print(f"La suma total es: {total}")

print('')

#Ejercicio 5 Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print ('Ejercicio 5')

import random 

bot_num = random.randint(0,10) # random
user_num5 = int(input('Ingresa un número entre 0 y 9: ')) # usuario

counter = 1 

while bot_num != user_num5:
    counter += 1
    user_num5 = int(input(f'{Fore.RED} INCORRECTO. ingresa otro número entre 0 y 9: '))

print(f'{Fore.GREEN} CORRECTO El número era {bot_num}')
print(f'Tuviste que intentarlo {counter} veces.')

print('')

#Ejercicio 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
print ('Ejercicio 6')

for num_6 in range(100, -1, -1): # 100 a 0 | con paso -1
    if num_6 % 2 == 0:
        print(num_6)

print('')

#Ejercicio 7 ) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
print ('Ejercicio 7')


user_num7 = int(input('Ingrese el número: '))

counter = 1
result = 0

while counter < user_num7:  # mientras no lleguemos a user_num7 (num anterior)
    result += counter
    counter += 1 

print(f'La suma entre los números comprendidos entre 0 y {user_num7} es: {result}')

print('')

#Ejercicio 8
#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print ('Ejercicio 8')

even = 0 # par
odd = 0 # impar
negative = 0 # positivo
positive = 0 # negativo


for user_num8 in range(100):
    user_num8 = int(input('Ingrese un número: '))

    if user_num8 % 2 == 0: # PAR
        even += 1
    elif user_num8 % 2 != 0: # IMPAR
        odd += 1
    
    if user_num8 < 0: # NEGATIVO
        negative += 1
    elif user_num8 > 0: # POSITIVO
        positive += 1

print(f' Los números pares ingresados son: {even} \n ' 
f'Los números impares ingresados son: {odd} \n ' 
f'Los números negativos ingresados son: {negative}\n ' 
f'Los números positivos ingresados son: {positive} \n ')

print('')

#Ejercicio 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
print ('Ejercicio 9')

from statistics import mode, median, mean #moda, mediana, media

numbers = [] # lista para ir guardando los numeros del usuario

for counter_9 in range(5):
    user_num9 = int(input('Ingrese un número: '))
    numbers.append(user_num9) # va a ir guardando los numeros en la lista

user_mean = mean(numbers)

print(f'La media de los números ingresados es: {user_mean}')

print('')

#Ejercicio 10 scribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print ('Ejercicio 10')

reversed_num = 0

user_num10 = input ('Ingrese un número: ')
if user_num10.isdigit():
    reversed_num = user_num10[::-1] # slicing para invertir el orden (forma mas sencilla)
    print(f'El número invertido es: {int(reversed_num)}')

else:
    print('No es un número.')

""" while user_num10 > 0:
    digit = user_num10 % 10       # tomo el último dígito
    reversed_num = reversed_num * 10 + digit  # lo voy agregando al invertido
    user_num10 //= 10             # elimino el último dígito """ # forma matematica

print('')
