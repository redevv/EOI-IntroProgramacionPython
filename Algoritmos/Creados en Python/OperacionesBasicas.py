# 4. Realizar las cuatro operaciones básicas (Suma, Resta, Multiplicación, División).

Num1=input("Inserte primer número: ")
Op=input("Inserte operación: ")
Num2=input("Inserte segundo número: ")
Num1=float(Num1)
Num2=float(Num2)
try:
    if (Op=="+"):
        print(Num1+Num2)
    elif (Op=="-"):
        print(Num1-Num2)
    elif (Op=="*"):
        print(Num1*Num2)
    else:
        print(Num1/Num2)
except ZeroDivisionError: # Errores personalizados tienen prioridad y han de ponerse primero.
    print("Error al dividir por cero") 
# Fin Algoritmo