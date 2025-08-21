# Pedir al usuario un número
numero = int(input("Ingrese un número: "))

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")