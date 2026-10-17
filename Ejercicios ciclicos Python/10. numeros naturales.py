"""
10.. Escribir un programa que multiplique 
los 20 primeros números naturales.
Ejemplo: (1*2*3*4*5…).  
"""
resultado = 1
for i in range(1, 21):
    resultado *= i
    print(f" Factorial de {i} === La multiplicación de los 20 primeros números naturales es: {resultado}")
