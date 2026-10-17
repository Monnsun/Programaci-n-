#8. Tomando como base los resultados obtenidos
# en un laboratorio de análisis clínicos, un médico determina 
# si una persona tiene anemia o no, lo cual depende de su nivel 
# de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel 
# de hemoglobina que tiene una persona es menor que el rango que le 
# corresponde, se determina su resultado como positivo y en caso 
# contrario como negativo. La tabla en la que el médico se basa 
# para obtener el resultado es la siguiente:
# EDAD NIVEL HEMOGLOBINA 

# 0 - 1 mes     13 - 26 g% 
# > 1 y < = 6 meses  10 - 18 g% 
# > 6 y < = 12 meses 11 - 15 g% 
# > 1 y < = 5 años   11.5 - 15 g% 
# > 5 y < = 10 años  12.6 - 15.5 g% 
# > 10 y < = 15 años 13 - 15.5 g% 
# mujeres > 15 años 12 - 16 g% 
# hombres > 15 años  14 - 18 g% 

hemoglobina = int(input("ingrese el nivel de hemoglobina: "))
mayor = int(input("es mayor a 1 año? 1=si 2=no: "))
if mayor == 2:
    meses = int(input("ingrese la cantidad de meses: "))
    if meses <= 1:
        if hemoglobina < 13:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")
    elif meses > 1 and meses <= 6:
        if hemoglobina < 10:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")
    else:
        if hemoglobina < 11:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")
else:
    edad = int(input("ingrese la edad: "))
    if edad > 15:
        sexo = int(input("ingrese el sexo 1=masculino 2=femenino: "))
        if sexo == 1:
            if hemoglobina < 14:
                print(" tiene anemia")
            else:
                print(" no tiene anemia")
        else:
            if hemoglobina < 12:
                print(" tiene anemia")
            else:
                print(" no tiene anemia")
    elif edad > 1 and edad <= 5:
        if hemoglobina < 11.5:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")
    elif edad > 5 and edad <= 10:
        if hemoglobina < 12.6:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")
    elif edad > 10 and edad <= 15:
        if hemoglobina < 13:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")
    else:
        if hemoglobina < 13:
            print(" tiene anemia")
        else:
            print(" no tiene anemia")  