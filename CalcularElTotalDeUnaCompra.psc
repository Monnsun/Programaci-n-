# Calcular el total de una compra

print("Para calcular el total de su compra ingrese los datos solicitados a continuación")
print("Ingrese el nombre de cada producto y el precio, además de la cantidad por cada producto")


print("Ingrese el nombre del producto 1")
p1 = input()
print("Ingrese el precio")
precio1 = float(input())
print("Ingrese cuantas", p1, "compro")
cantidad_p1 = float(input())
cantidad1 = precio1 * cantidad_p1

print("Ingrese el nombre del producto 2")
p2 = input()
print("Ingrese el precio")
precio2 = float(input())
print("Ingrese cuantas", p2, "compro")
cantidad_p2 = float(input())
cantidad2 = precio2 * cantidad_p2


print("Ingrese el nombre del producto 3")
p3 = input()
print("Ingrese el precio")
precio3 = float(input())
print("Ingrese cuantas", p3, "compro")
cantidad_p3 = float(input())
cantidad3 = precio3 * cantidad_p3

total_compra = cantidad1 + cantidad2 + cantidad3

print("**********************")
print("Su total de compra es..")
print(p1, cantidad1, "COP")
print(p2, cantidad2, "COP")
print(p3, cantidad3, "COP")
print("Total de la compra", total_compra, "COP")
print("**********************")