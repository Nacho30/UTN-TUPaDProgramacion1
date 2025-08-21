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