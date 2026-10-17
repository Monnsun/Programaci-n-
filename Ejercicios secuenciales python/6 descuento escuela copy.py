# Se ha establecido un programa para estimular a los alumnos,
# el cual consiste en lo siguiente: si el promedio obtenido 
# por un alumno en el último periodo es mayor o igual que 4.0, 
# se le hará un descuento del 30% sobre la pensión; 
# si el promedio obtenido es menor que 4.0 deberá pagar la pensión completa,
# la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno. 

promedio = int (input("ingrese el promedio de sus notas:  "))
pension = int (input("ingrese el valor de la pensión:  "))
if promedio >= 4.0 :
    descuento = 0.30
    total = pension * descuento
    pagar = pension - total
    print("El alumno tiene un descuento del 30% sobre la pensión")
    print("El valor del descuento es: ", total)
    print("El valor a pagar es: ", pagar)
elif promedio < 4.0:
    print("El alumno no tiene descuento y debe pagar la pensión completa")
    print("El valor de la pensión completa es: ", pension)
