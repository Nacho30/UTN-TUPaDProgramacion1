# Ejercicio 1 Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

print('Ejercicio 1')

multiple_4 = []

for i in range(1, 101):
    if i % 4 == 0:
        multiple_4.append(i) # agrega i a la lista

# print(multiple_4)  [El ejercicio nunca pide que se muestre]

print('')

# Ejercicio 2  Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

print('Ejercicio 2')

list = ['Marcelo', 'Benito', 'Wazo', 'Nacho', 'Hola']

print(list[-2])  # el elemento 3 ó -2

print('')

# Ejercicio 3 ) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []
print('Ejercicio 3')

empty_list = []

empty_list.append('COLSA')
empty_list.append('CAMPUS')
empty_list.append('UTN')

print (empty_list)

print('')

# Ejercicio Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

print('Ejercicio 4')

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = 'capibara'
animales[3] = 'tortuga' # no es necesario usar remove y luego insert

print(animales)

print('')

# Ejercicio 5 Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
print('Ejercicio 5')

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Lo que hace el ejercicio es remover con el .remove el numero mas alto de la lista numeros, (en este caso el 22)

print('')

# Ejercicio 6  Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
print('Ejercicio 6')

number_list = []

for i in range(10, 31, 5): # number_list = list(range(10, 31, 5))
    number_list.append(i)

print(number_list[:2])
    

print('')

# Ejercicio 7 Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]
print('Ejercicio 7')

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = 'Renault'
autos[2] = 'Merceedes'

# print (autos)

print('')

# Ejercicio 8 Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

print('Ejercicio 8')

dobles = []

for i in range(5, 16, 5):
    i *= 2
    dobles.append(i)

print(dobles)

print('')

# Ejercicio 9 Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

print('Ejercicio 9')

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# cliente 1: pan / leche
# cliente 2: arroz / fideos / salsa
# cliente 3: agua

compras[2].append('jugo')
compras[1][1] = 'tallarines'
compras[0].remove('pan')

print(compras)

print('')

# Ejercicio 10
print('Ejercicio 10')

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print (lista_anidada)

print('')

