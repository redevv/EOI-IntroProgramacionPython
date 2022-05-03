# 9. Encontrar si un número es mayor o menor a uno dado.

Num1=input("Ingrese primer número: ")
Num2=input("Ingrese segundo número: ")
Num1=float(Num1)
Num2=float(Num2)
try:
    if (Num1>Num2):
        print(f"{Num1} es mayor")
    else:
        print(f"{Num2} es mayor")
    # Fin if
except ValueError:
    print("Por favor, ingrese valor numérico")
# Fin Algoritmo