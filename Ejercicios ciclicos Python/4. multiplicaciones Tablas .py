"""Calcular e imprimir la tabla 
    de multiplicar de un número cualquiera, 
    el cual se digitará por teclado. Imprimir 
    el multiplicando, el multiplicador y el producto. 
"""
i=0
num = int(input("Ingrese un número para calcular su tabla de multiplicar: "))
print(f"============== Tabla de multiplicar del número {num} ===============")
while i < 11:
    producto = num * i
    print(f"- {num} x {i} = {producto} ")
    i += 1
print("=====================================================================")