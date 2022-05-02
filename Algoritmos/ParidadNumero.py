# 3. A partir de un número ingresado diga si el mismo es par o impar:

nro=input("Ingrese un número:")
if (nro.isdigit()):
    nro=int(nro)
    if (nro%2==0):
        print("Es par")
    else:
        print("Es impar")
else:
    print("Por favor, introduzca un número válido")
    # Fin if
# Fin Algoritmo