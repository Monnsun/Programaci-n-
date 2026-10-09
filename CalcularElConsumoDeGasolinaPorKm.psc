# Calcular el consumo de gasolina por km

print("Calcular el consumo de gasolina por km. Ingrese la gasolina (L) y los km recorridos")

print("Ingrese la gasolina (L)")
gasolina = float(input())

print("Ingrese los km recorridos")
km = float(input())

formula = gasolina / km

print("El consumo de gasolina sobre km es", formula, "L/km")