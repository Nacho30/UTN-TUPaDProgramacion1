ingreso_a_sistema = input("Bienvenido al sistema de calculadora de restaurante. ¿Cuál es su nombre?")
print("Hola", ingreso_a_sistema)
ingresa_cuenta = float(input("Por favor, ingrese el total de su cuenta: "))
propina_10 = ingresa_cuenta * 0.10
propina_15 = ingresa_cuenta * 0.15
total_con_propina_10 = ingresa_cuenta + propina_10
total_con_propina_15 = ingresa_cuenta + propina_15
print("El total de su cuenta sin propina es de: $", ingresa_cuenta)
print("El total de su cuenta con propina del 10% es de: $", total_con_propina_10)
print("El total de su cuenta con propina del 15% es de: $", total_con_propina_15)
