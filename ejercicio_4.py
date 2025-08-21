# Pedir al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área y el perímetro
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio

# Imprimir los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")