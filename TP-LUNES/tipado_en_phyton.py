clases={"lunes": "nivel inicial",
    "martes": "nivel intermedio",
    "miercoles": "nivel avanzado",
    "jueves": "practica hablada",
    "viernes": "ingles para viajeros"
}

dias_validos = list(clases.keys())

fecha_actual = input("Ingrese la fecha actual (dia, dd/mm): ")
fecha_actual = fecha_actual
dia_semana = fecha_actual.split(", ")[0].lower()
if dia_semana not in dias_validos:
    print("Día inválido. Por favor, ingrese un día válido de la semana.")
    exit()
dia,mes = fecha_actual.split(", ")[1].split("/")
dia = int (dia)
mes = int (mes)

if not (1 <= dia <= 31 and 1 <= mes <= 12):
    print("Fecha inválida. Por favor, ingrese una fecha en formato dd/mm.")
    exit()
nivel = clases [dia_semana]
print(f"El día {dia}/{mes} es {dia_semana.capitalize()} y la clase es de nivel {nivel}.")
if nivel in ["nivel inicial", "nivel intermedio", "nivel avanzado"]:
    hubo_examen = input("¿Hubo examen hoy? (si/no): ").lower()
    if hubo_examen == "si":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = aprobados + desaprobados
        if total_alumnos > 0:
            porcentaje_aprobados = (aprobados / total_alumnos) * 100
            print(f"Porcentaje de alumnos aprobados: {porcentaje_aprobados:.2f}%")
        else:
            print("No se ingresaron alumnos.")
elif nivel == "practica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia: "))
    if asistencia >= 50:
        print("Bien asistio la mayoria")
    else:
        print("No asistio la mayoria")
elif nivel == "ingles para viajeros":
    if dia == 1 and (mes==1 or mes == 7):
     print ("Comienzo del nuevo ciclo")
     alumnos = int(input("Ingrese la cantidad de alumnos inscriptos: "))
     arancel = int(input("Ingrese el arancel por almno en $ "))
     ingreso_total = alumnos * arancel
     print(f"Ingreso total por inscripciones: ${ingreso_total:.2f}")
