"""Una persona debe realizar un muestreo con 50 personas
para determinar el promedio de peso de los niños, jóvenes, 
adultos y ancianos que existen en su zona. Las categorías 
se determinar de acuerdo a la siguiente tabla:  
"""
i = 0
niños = 0
jóvenes = 0
adultos = 0
ancianos = 0
cantidad_niños = 0
cantidad_jóvenes = 0
cantidad_adultos = 0
cantidad_ancianos = 0

while i < 5:
    edad = int(input(f"Persona {i} -  ingrese la edad de la persona: "))
    peso = float(input(f"Persona {i} -  ingrese el peso de la persona: "))
    i += 1
    if edad < 12:
        niños += peso
        cantidad_niños += 1
    elif edad < 26:
        jóvenes += peso
        cantidad_jóvenes += 1
    elif edad < 56:
        adultos += peso
        cantidad_adultos += 1
    else:
        ancianos += peso
        cantidad_ancianos += 1
while True:
    
    print("===== MENÚ =======================================")
    print("1. promedio de peso de niños")
    print("2. promedio de peso de jóvenes")
    print("3. promedio de peso de adultos")
    print("4. promedio de peso de ancianos")
    print("5. salir")
    print("==================================================")

    opcion = input("Elige una opción (1-5): ")
    if opcion == "1":
        print(f"Promedio de peso de niños: {niños/cantidad_niños if cantidad_niños > 0 else 0}")
        
    elif opcion == "2":
        print(f"Promedio de peso de jóvenes: {jóvenes/cantidad_jóvenes if cantidad_jóvenes > 0 else 0}")
    elif opcion == "3":
        print(f"Promedio de peso de adultos: {adultos/cantidad_adultos if cantidad_adultos > 0 else 0}")
    elif opcion == "4":
        print(f"Promedio de peso de ancianos: {ancianos/cantidad_ancianos if cantidad_ancianos > 0 else 0}")
    elif opcion == "5":
        print("=== Has elegido salir.")
        break
    else:
        print("==== Opción no válida. Intenta de nuevo.")