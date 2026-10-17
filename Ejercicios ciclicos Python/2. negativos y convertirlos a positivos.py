#Leer 10 números negativos y convertirlos a 
# positivos e imprimir la suma de dichos números. 
i = 0
suma = 0
while i < 10:
    num = int(input(f"Numero {i} -  ingrese un numero negativo: "))
    num = -num
    suma += num
    i += 1
print(f"La suma de los numeros convertidos a positivos es: {suma}")
