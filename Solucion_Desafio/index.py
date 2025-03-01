calificacion2 = []


for i in range(5):
    calificacion1 = float(input("Ingresa la calificación: "))
    calificacion2.append(calificacion1)


promedio = sum(calificacion2) / len(calificacion2)


if promedio >= 60:
    resultado = "Aprobado"

elif 40 <= promedio < 60:
    resultado = "En recuperación"
    
else:
    resultado = "Reprobado"


print(f"\nEl promedio de las calificaciones es: {promedio}")
print(f"Resultado: {resultado}")