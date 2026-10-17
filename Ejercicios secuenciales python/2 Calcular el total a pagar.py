#Calcular el total a pagar por la compra de zapatillas. 
# Si se compran tres  o más zapatillas se aplica un descuento del 20% 
# sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%.
# Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar 
# una vez aplicado el descuento. 

valor = int(input("= Ingrese el valor total de la compra: "))   
cantidad = int(input("= Ingrese la cantidad de zapatillas: "))
if cantidad >= 3:
    descuento = valor * 0.20
    total = valor - descuento
    print("= Valor de la compra: ", valor)
    print("= Valor del descuento: ", descuento)
    print("= Valor a pagar: ", total)
else:
    descuento = valor * 0.10
    total = valor - descuento
    print("= Valor de la compra: ", valor)
    print("= Valor del descuento: ", descuento)
    print("= Valor a pagar: ", total)