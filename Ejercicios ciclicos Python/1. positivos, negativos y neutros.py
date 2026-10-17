#Leer 20 números e imprimir cuantos 
# son  positivos, cuantos negativos 
# y cuantos neutros. 

i = 0
positivos = 0
negativos = 0
neutros = 0

while i < 20:
    num = int(input(f"Numero {i + 1} -  ingrese numeros positivos, negativos y neutros: "))
    i += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Neutros: {neutros}")
