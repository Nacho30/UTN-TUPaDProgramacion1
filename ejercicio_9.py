# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Calcular la temperatura en grados Fahrenheit
fahrenheit = (9/5) * celsius + 32

# Imprimir el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")