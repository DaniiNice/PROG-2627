nota = int(input("Cuanto porcentaje tienes en el examen final?: "))
asistencia = int(input("Cuanto porcentaje de asistencia tienes?: "))

if nota >= 60 and asistencia >= 80:
    print("Tienes aprobado el curso")
else:
    print("Tienes suspenso el curso")