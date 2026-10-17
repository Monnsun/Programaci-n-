"""
9.  Calcular el promedio de edades de hombres, 
mujeres y de todo un grupo de alumnos.  

"""

grupo = int(input ("Ingrese la cantidad de personas en el grupo "))
n=0
edad_hombres = 0
hombres = 0
edad_mujeres = 0
mujeres = 0
total_edad = 0
i=0
while grupo > n:
    genero = input(f"Ingrese el género de la persona {i+1} (hombre/mujer): ")
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    total_edad += edad
    if genero == "hombre":
        edad_hombres += edad
        hombres += 1
    elif genero == "mujer":
        edad_mujeres += edad
        mujeres += 1
    n += 1

promedio_total = total_edad / grupo
promedio_hombres = edad_hombres / hombres if hombres > 0 else 0
promedio_mujeres = edad_mujeres / mujeres if mujeres > 0 else 0

while True:
    
    print("===== MENÚ =======================================")
    print("1. ver promedio de edades de hombres")
    print("2. ver promedio de edades de mujeres")
    print("3. ver promedio de edades del grupo")
    print("4. salir")
    print("==================================================")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"=== Has elegido ver promedio de edades de hombres: {promedio_hombres}")
    elif opcion == "2":
        print(f"=== Has elegido ver promedio de edades de mujeres: {promedio_mujeres}")
    elif opcion == "3":
        print(f"=== Has elegido ver promedio de edades del grupo: {promedio_total}")    
    elif opcion == "4":
        print("=== Has elegido salir.")
        break
    else:
        print("==== Opción no válida. Intenta de nuevo.")

