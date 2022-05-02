# 6. Ingrese un número y muestre todos los divisores del mismo.

while (True):
    Num=input("Ingrese Número (N para salir): ")
    div=1
    if (Num.isdigit()):
        Num=int(Num)
        while (div<=Num):
            if (Num%div==0):
                print(div)
            # Fin if
            # div=div+1
            div+=1
        # Fin while
    else:
        if (Num=="N"):
            break
        print("Por favor, introduzca un valor numérico")
# Fin Algoritmo