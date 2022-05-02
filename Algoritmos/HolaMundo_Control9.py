# 1. "Hola Mundo"

# print("Hola Mundo")


# 2. "A partir de un número ingresado diga si es mayor, menor o igual a 9"

print("Escribir el número:")
N=input()
if (N.isdigit()): # Para certificar que el valor es numérico.
    N=float(N)
    if(N==9):
        print("El número es igual a 9")
    else:
        if(N>9):
            print("El número es mayor a 9")
        else:
            print("El número es menor a 9")
else:
    print("Por favor, introduzca un número")
        # Fin if
    # Fin if
# Fin Algoritmo
