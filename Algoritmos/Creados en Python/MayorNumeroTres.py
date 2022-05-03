# 7. Encontrar el número mayor de tres números.

Num1=input("Ingrese primer número: ")
Num2=input("Ingrese segundo número: ")
Num3=input("Ingrese tercer número: ")
Num1=float(Num1)
Num2=float(Num2)
Num3=float(Num3)
if (Num1>Num2):
    if (Num1>Num3):
        print(Num1)
    else:
        print(Num3)
    # Fin if
else:
    if (Num2>Num3):
        print(Num2)
    else:
        print(Num3)
    # Fin if
# Fin if
# Fin Algoritmo