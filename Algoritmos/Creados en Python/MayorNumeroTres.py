# 7. Encontrar el número mayor de tres números.

Num1=input("Ingrese primer número: ")
Num2=input("Ingrese segundo número: ")
Num3=input("Ingrese tercer número: ")
if (Num1.isdigit() and Num2.isdigit() and Num3.isdigit()):
    Num1=float(Num1)
    Num2=float(Num2)
    Num3=float(Num3)
    if (Num1>Num2):
        if (Num1>Num3):
            print(f"El número mayor es el {Num1}")
        else:
            print(f"El número mayor es el {Num3}")
        # Fin if
    else:
        if (Num2>Num3):
            print(f"El número mayor es el {Num2}")
        else:
            print(f"El número mayor es el {Num3}")
        # Fin if
    # Fin if
else:
    print("Por favor, introduzca valor numérico")
# Fin Algoritmo