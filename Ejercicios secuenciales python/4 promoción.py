#En un supermercado se hace una promoción,
# mediante la cual el cliente obtiene un descuento dependiendo de un color  
# que se escoge al azar. Si el color de la balota es rojo  el descuento es 
# del 15% sobre el total de la compra, la balota es verde el descuento es del 20%.
# Si  el color es diferente a los indicados no obtendrá descuento.  
# Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar. 

monto = int (input("= Ingrese el valor total de la compra: "))
color = input("Ingrese el color de su balota:")
if color == "rojo":
    descuento = monto * 0.15
    total = monto - descuento
    print("= Valor de la compra: ", monto)
    print("= Color de la balota: ", color)
    print("= Valor del descuento: ", descuento)
    print("= Valor a pagar: ", total)
elif color == "verde":
    descuento = monto * 0.20
    total = monto - descuento
    print("= Valor de la compra: ", monto)
    print("= Color de la balota: ", color)
    print("= Valor del descuento: ", descuento)
    print("= Valor a pagar: ", total)
else:
    print("= Valor de la compra: ", monto)
    print("= Color de la balota: ", color)
    print("= No tiene descuento")
    print("= Valor a pagar: ", monto)
