"""
Calcular la cantidad de hombres y mujeres
presentes en un salón de clases con un
total de n personas. 
"""
n = int(input("Ingrese el total de personas en el salón: "))
i = 0
hombres = 0
mujeres = 0

while i < n:
    genero = input(f"Persona {i+1} - Ingrese el género (M/F): ")
    if genero == "M":
        hombres += 1
    elif genero == "F":
        mujeres += 1
    else:
        print("Género no válido. Por favor, ingrese 'M' o 'F'.")
        continue
    i += 1
    
while True:
    
    print("===== MENÚ =======================================")
    print("1. promedio hombres")
    print("2. promedio mujeres")
    print("3. salir")
    print("==================================================")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        print(f"=== Has elegido promedio de Hombres es : {hombres/n if hombres > 0 else 0}")
    elif opcion == "2":
        print(f"=== Has elegido promedio de Mujeres es : {mujeres/n if mujeres > 0 else 0}")
    elif opcion == "3":
        print("=== Has elegido salir.")
        break
    else:
        print("==== Opción no válida. Intenta de nuevo.")
