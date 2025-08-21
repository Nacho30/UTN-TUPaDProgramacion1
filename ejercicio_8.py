# Pedir al usuario su altura y peso
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Calcular el índice de masa corporal
imc = peso / (altura ** 2)

# Imprimir el resultado
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")