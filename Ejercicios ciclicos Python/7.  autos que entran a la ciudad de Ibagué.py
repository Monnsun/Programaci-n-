"""
La oficina de tránsito de Ibagué desea saber, 
de los n autos que entran a la ciudad de Ibagué,  
cuantos entran con calcomanía de cada color. 
Conociendo el ultimo dígito de la placa de cada carro,
se puede determinar el color de la calcomanía utilizando la siguiente relación:  
"""

n = int(input("Ingrese el número de autos que entran a la ciudad de Ibagué: "))
amarillo = 0
rosa= 0
rojo = 0
verde = 0
azul = 0

while n > 0:
    placa = input(f"Auto numero {n}, Ingrese el último dígito de la placa del auto: ")
    if placa == "1" or placa == "2":
        amarillo += 1
    elif placa == "3" or placa == "4":
        rosa += 1
    elif placa == "5" or placa == "6":
        rojo += 1
    elif placa == "7" or placa == "8":
        verde += 1
    elif placa == "9" or placa == "0":
        azul += 1

    n -= 1

while True:
    
    print("===== MENÚ =======================================")
    print("1. color de calcomania amarilla")
    print("2. color de calcomania rosa")
    print("3. color de calcomania roja")
    print("4. color de calcomania verde")
    print("5. color de calcomania azul")
    print("6. salir")
    print("==================================================")

    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":
        print(f"=== Has elegido color de calcomania amarilla: {amarillo}")
    elif opcion == "2":
        print(f"=== Has elegido color de calcomania rosa: {rosa}")
    elif opcion == "3":
        print(f"=== Has elegido color de calcomania roja: {rojo}")
    elif opcion == "4":
        print(f"=== Has elegido color de calcomania verde: {verde}")
    elif opcion == "5":
        print(f"=== Has elegido color de calcomania azul: {azul}")
    elif opcion == "6":
        print("=== Has elegido salir.")
        break
    else:
        print("==== Opción no válida. Intenta de nuevo.")

