"""
11. Pedir los datos de los alumnos, estos 
son: sexo, edad y altura. Al final del programa 
se deberá mostrar la cantidad de hombres, la cantidad 
de mujeres, la altura promedio ,la cantidad de alumnos
que tienen una altura mayor a 1.70 cm, la cantidad de
alumnos que tiene una altura menor o igual a 1.50 cm.
El programa debe finalizar cuando la edad sea igual a 0. 
"""
hombres = 0
altura_hombres = 0
mujeres = 0
altura_mujeres = 0
total_altura = 0
altura_mayor_170 = 0
altura_menor_igual_150 = 0

grupo = int(input("Ingrese la cantidad de alumnos en el grupo: "))
for i in range(grupo):
    genero = input(f"Ingrese el género del alumno {i} (hombre/mujer): ")
    edad = int(input(f"Ingrese la edad del alumno {i} (0 para finalizar): "))
    if edad == 0:
        print("=== Programa finalizado por edad igual a 0.")
        break
    altura = float(input(f"Ingrese la altura del alumno {i} en metros: "))

    total_altura += altura

    if genero == "hombre":
        hombres += 1
        altura_hombres += altura
    elif genero == "mujer":
        mujeres += 1
        altura_mujeres += altura

    if altura > 1.70:
        altura_mayor_170 += 1
    elif altura <= 1.50:
        altura_menor_igual_150 += 1

if hombres > 0:
    promedio_hombres = altura_hombres / hombres
else:
    promedio_hombres = 0

if mujeres > 0:
    promedio_mujeres = altura_mujeres / mujeres
else:
    promedio_mujeres = 0

if grupo > 0:
    promedio_general = total_altura / grupo
else:
    promedio_general = 0
    
while True:
    print("===== MENÚ =======================================")
    print("1. ver cantidad  de hombres")
    print("2. ver cantidad  de mujeres")
    print("3. ver Altura promedio del grupo")
    print("4. Cantidad de alumnos con altura mayor a 1.70 cm")
    print("5. Cantidad de alumnos con altura menor o igual a 1.50 cm")
    print("6. salir")
    print("==================================================")

    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":
        print(f"=== Has elegido ver cantidad  de hombres: {hombres}")
    elif opcion == "2":
        print(f"=== Has elegido ver cantidad     de mujeres: {    mujeres}")
    elif opcion == "3":
        print(f"=== Has elegido ver Altura promedio del grupo: {promedio_general}")    
    elif opcion == "4":
        print(f"=== Has elegido ver Cantidad de alumnos con altura mayor a 1.70 cm: {altura_mayor_170}")
    elif opcion == "5":
        print(f"=== Has elegido ver Cantidad de alumnos con altura menor o igual a 1.50 cm: {altura_menor_igual_150}")
    elif opcion == "6":
        print("=== Has elegido salir.")
        break   
    else:
        print("==== Opción no válida. Intenta de nuevo.")
        
