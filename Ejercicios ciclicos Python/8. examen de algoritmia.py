"""8.un grupo de 23 estudiantes presentan un examen de 
algoritmia. Hacer un algoritmo que lea por cada estudiante 
la calificación obtenida. Al finalizar calcule e imprima: 

• La cantidad de estudiantes que obtuvieron una calificación
menor a 50.  

• La cantidad de estudiantes que obtuvieron una 
calificación de 50 o más pero menor que 70. 

• La cantidad deestudiantes que obtuvieron
una calificación de 70 o más pero
menor que 80.  

• La cantidad de estudiantes que obtuvieron 
unacalificación de 80 o más.

La calificación 
obtenida en el examen de algoritmia debe ser
entre 1 y 100. 
"""
estudiantes = 5
menor_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_80 = 0

for i in range(estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i}: "))
    while calificacion < 1 or calificacion > 100:
        print("La calificación debe ser entre 1 y 100. Intente de nuevo.")
        calificacion = float(input(f"Ingrese la calificación del estudiante {i}: "))
    
    if calificacion < 50:
        menor_50 += 1
    elif calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_80 += 1

while True:
    
    print("===== MENÚ =======================================")
    print("1. ver cantidad de estudiantes con calificación menor a 50")
    print("2. ver cantidad de estudiantes con calificación de 50 o más pero menor que 70")
    print("3. ver cantidad de estudiantes con calificación de 70 o más pero menor que 80")
    print("4. ver cantidad de estudiantes con calificación de 80 o más")
    print("5. salir")
    print("==================================================")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        print(f"=== Has elegido ver cantidad de estudiantes con calificación menor a 50: {menor_50}")
    elif opcion == "2":
        print(f"=== Has elegido ver cantidad de estudiantes con calificación de 50 o más pero menor que 70: {entre_50_y_70  }")
    elif opcion == "3":
        print(f"=== Has elegido ver cantidad de estudiantes con calificación de 70 o más pero menor que 80: {entre_70_y_80}")
    elif opcion == "4":
        print(f"=== Has elegido ver cantidad de estudiantes con calificación de 80 o más: {mayor_80}")
    elif opcion == "5":
        print("=== Has elegido salir.")
        break
    else:
        print("==== Opción no válida. Intenta de nuevo.")
