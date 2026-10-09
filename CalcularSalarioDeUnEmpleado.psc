# Calcular el salario de un empleado

salario_base = 1750.950
auxilio_de_transporte = 249.095

print("A continuación podrás calcular el salario Base...")

print("Ingrese lo que ganaste como horas extras")
extras = float(input())

print("Ingrese el valor (mensual) del seguro de Salud")
salud = float(input())

print("Ingrese el valor (mensual) del Seguro de Pension")
pension = float(input())

salario_neto = (salario_base + extras + auxilio_de_transporte) - (salud + pension)

print("El salario Neto es", salario_neto)