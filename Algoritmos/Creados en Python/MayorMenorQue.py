# 9. Encontrar si un número es mayor o menor a uno dado.

Num1=float(7.5)
print(f"Número dado: {Num1}")

Num2=input("Ingrese un número: ")
if (Num2.isdigit()):
    Num2=float(Num2)
    if (Num1>Num2):
        print(f"{Num1} es mayor que {Num2}")
    else:
        print(f"{Num2} es mayor que {Num1}")
    # Fin if
else:
    print("Por favor, ingrese valor numérico")
# Fin Algoritmo