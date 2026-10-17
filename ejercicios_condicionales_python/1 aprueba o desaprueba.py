# Determinar si un aprendiz aprueba o desaprueba Algoritmia, 
# sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 70; 
# reprueba en caso contrario. 

print("= Ingrses sus notas entre 100 y 0 ==================================I")
nota1 = int(input("= Ingrese el numero de su primera nota: "))
nota2 = int(input("= Ingrese el numero de su segunda nota: "))
nota3 = int(input("= Ingrese el numero de su tercera nota: "))
nota = (nota1 + nota2 + nota3) // 3
if nota >= 70:
    print("= Aprobado, su promedio es: ", nota)
else:
    print("= Desaprobado, su promedio es: ", nota)
