# Calcular el número de pulsaciones que debe 
# tener una persona por cada 10 segundos de ejercicio aeróbico; 
# la fórmula que se aplica es:  cuando el sexo 
# es femenino : núm. pulsaciones = (220 - edad)/10  y
# si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 

sexo = (input("Ingrese su sexo (femenino o masculino): "))
edad = int(input("Ingrese su edad: "))
if sexo == "femenino":
    pulsaciones = (220 - edad) / 10
    print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: ", pulsaciones)
elif sexo == "masculino":
    pulsaciones = (210 - edad) / 10
    print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: ", pulsaciones)
else:
    print("Sexo no válido. Por favor, ingrese 'femenino' o 'masculino'.")
