'''
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio  y la calificación
más alta y  más baja de todo el grupo.  
'''
i = 0
num = 0
suma = 0
calificaciones = []
while i < 5:
    num = int(input(f"Alumno Numero {i} -  ingrese las notas del alumno: "))
    i += 1
    suma += num
    calificaciones.append(num)
    
while True:
    
    print("===== MENÚ =======================================")
    print("1. promedio de calificaciones")
    print("2. calificación más alta")
    print("3. calificación más baja")
    print("4. Salir")
    print("==================================================")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        promedio = suma / 20
        print(f"==== Has elegido promedio de calificaciones. El promedio es: {promedio}")
    elif opcion == "2":
        calificacion_alta = max(calificaciones)
        print(f"=== Has elegido calificación más alta. La calificación más alta es: {calificacion_alta}\n")
    elif opcion == "3":
        calificacion_baja = min(calificaciones)
        print(f"=== Has elegido calificación más baja. La calificación más baja es: {calificacion_baja}\n")
    elif opcion == "4":
        print("==== Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("==== Opción no válida. Intenta de nuevo.")
