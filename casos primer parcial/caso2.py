#Caso 2 – Clínica – Turnos por especialidad (cupos del día)
#Enunciado / Descripción
#Una clínica desea administrar eficientemente las diferentes especialidades médicas que ofrece
#  y la disponibilidad de cupos (espacios para citas) diarios para cada una. 
# Se pide implementar un programa que utilice listas paralelas: una lista especialidades[] para almacenar los nombres 
# de las especialidades (e.g., "Cardiología", "Dermatología") y otra lista cupos[] para almacenar el número de cupos
# disponibles para cada especialidad en un día específico. Ambas listas deben compartir el mismo índice, 
# de manera que el cupo en cupos[i] corresponda a la especialidad en especialidades[i]. El programa debe presentar un menú 
# al usuario y utilizar un bucle while para permitirle realizar diferentes operaciones hasta que elija la opción "Salir".
bienvenida = ("Bienvenido a la gestión de turnos de la clínica")
print(bienvenida)
especialidades = ["Cardiología", "Dermatología", "Pediatría", "Neurología", "Otorrinolaringología"]
cupos = [5, 3, 4, 2, 6]
while True:
    print("\nMenú de opciones:")
    print("1. Ver especialidades y cupos disponibles")
    print("2. Agregar cupos a una especialidad")
    print("3. Agregar nueva especialidad")
    print("0. Salir")
    
    menu = int(input("Seleccione una opción (0-3): "))
    
    if menu == 0:
        print("¡Hasta luego!")
        break
    elif menu == 1:
        print("Especialidades y cupos disponibles:")
        for i in range(len(especialidades)):
            print(f"{especialidades[i]}: {cupos[i]} cupos disponibles")
    elif menu == 2:
        especialidad = input("Ingrese el nombre de la especialidad: ")
        if especialidad in especialidades:
            indice = especialidades.index(especialidad)
            nuevos_cupos = int(input("Ingrese la cantidad de nuevos cupos: "))
            cupos[indice] += nuevos_cupos
            print(f"Se han agregado {nuevos_cupos} cupos a {especialidad}.")
        else:
            print("Especialidad no encontrada.")
    elif menu == 3:
        nueva_especialidad = input("Ingrese el nombre de la nueva especialidad: ")
        if nueva_especialidad not in especialidades:
            cupos_nuevos = int(input("Ingrese la cantidad de cupos para la nueva especialidad: "))
            especialidades.append(nueva_especialidad)
            cupos.append(cupos_nuevos)
            print(f"Se ha agregado la especialidad {nueva_especialidad} con {cupos_nuevos} cupos.")
        else:
            print("La especialidad ya existe.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")