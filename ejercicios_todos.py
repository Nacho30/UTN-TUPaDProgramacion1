#Ejercicio 1
print(f"hola mundo")
#Ejercicio 2
nombre = (input("Ingrese su nombre: "))

print(f"Hola : {nombre}")
#Ejercicio 3
nombre = (input("Ingrese su nombre: "))
apellido = (input("Ingrese su apellido: "))
edad = (input("Ingrese su edad: "))
residencia = (input("Ingrese su residencia: "))

print(f"Hola soy {nombre} {apellido} tengo {edad} años y provengo de {residencia}")
#Ejercicio 4
# Pedir al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área y el perímetro
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio

# Imprimir los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5
# Pedir al usuario la cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))

# Calcular las horas
horas = segundos // 3600

# Imprimir el resultado
print(f"{segundos} segundos equivalen a {horas} horas.")

#Ejercicio 6
# Pedir al usuario un número
numero = int(input("Ingrese un número: "))

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7
# Pedir al usuario dos números enteros distintos de 0
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Realizar las operaciones
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2

# Imprimir los resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La división de {num1} entre {num2} es: {division:.2f}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La resta de {num1} menos {num2} es: {resta}")

#Ejercicio 8
# Pedir al usuario su altura y peso
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Calcular el índice de masa corporal
imc = peso / (altura ** 2)

# Imprimir el resultado 
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Calcular la temperatura en grados Fahrenheit
fahrenheit = (9/5) * celsius + 32

# Imprimir el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#Ejercicio 10
# Pedir al usuario 3 números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Imprimir el resultado
print(f"El promedio de los 3 números es: {promedio:.2f}")