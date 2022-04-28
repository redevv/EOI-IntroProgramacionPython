# 10. Leer tres números; si el primero es negativo, debe imprimir la multiplicación de los tres y si no lo es, imprimirá la suma.

Num1=input("Ingrese número 1: ")
Num2=input("Ingrese número 2: ")
Num3=input("Ingrese número 3: ")
try:
    Num1=float(Num1)
    Num2=float(Num2)
    Num3=float(Num3)
    if(Num1<0):
        Resul=Num1*Num2*Num3
    else:
        Resul=Num1+Num2+Num3
    print(Resul)
    # Fin Si
except ValueError:
    print("Por favor, ingrese un número")
except:
    print("Error")

# Fin Algoritmo