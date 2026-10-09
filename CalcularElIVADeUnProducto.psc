# Calcular el IVA de un producto

print("Calcular el IVA de un producto... Ingrese el precio del producto")
producto_precio = float(input())

# El IVA equivale al 19% del precio de la compra
total = producto_precio + (producto_precio * 0.19)

print("Total+IVA", total, "COP")