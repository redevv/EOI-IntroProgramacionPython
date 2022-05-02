# 4. Ingrese dos números y devuelva el resultado de la suma entre ambos.

# Num1=39
# Num2=78
# print("Escribir el número 1:")
# print(Num1)
# print("Escribir el número 2:")
# print(Num2)
# Rta=Num1+Num2
# print("El resultado es:",Rta)
# Fin Algoritmo

Num1=input("Escribir el número 1: ")
Num2=input("Escribir el número 2: ")
if (Num1.isdigit() and Num2.isdigit()):
    # Num1=float(Num1)
    # Num2=float(Num2) 
    Rta=Num1+Num2
    print(f"El resultado es: {int(Num1)+int(Num2)}")
else:
    print("Los valores introducidos no son válidos")
# Fin Algoritmo