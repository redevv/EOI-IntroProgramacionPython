# 8. Crear algoritmo que permita ingresar un nombre y una cantidad numérica

# print("Ingresar nombre: ")
nombre=input("Ingresar nombre: ")
# print("Ingresar cantidad: ")
num=input("Ingresar cantidad: ")
if(num.isdigit()):
    num=int(num)
    # print((f"{nombre}\n")*int(num)) # Alternativa más eficiente para crear
    while (num>0):
       print(nombre)
       num=num-1
# Fin While
else:
    print("Introduzca cantidad numérica")
# Fin Algoritmo