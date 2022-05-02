# 11. Si un número ingresado es primo o no. (Un número es primo si es divisible únicamente por 1 y por sí mismo).

nro=input("Ingrese un número: ")
div=2
band=True
if(nro.isdigit()):
    nro=int(nro)
    if (nro==1):
        print("Es primo")
    else:
        while (band==True and nro>div):
            if (nro%div==0):
                band=False
    # Fin if
    div+=1
    # Fin while
    if (band==True):
        print("Es primo")
    else:
        print("No es primo")
    # Fin if
else:
    print("Por favor, introduzca valor numérico")
# Fin if
# Fin Algoritmo
