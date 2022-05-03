# 2. Números primos.

nro=input("Ingrese un número: ")
div=2
band=True # Booleano para comprobar si el número es primo.
if(nro.isdigit()):
    nro=int(nro)
    if (nro==1):
        print("Es primo")
    else:
        while band and (nro>div): # band == True es equivalente a band.
            if (nro%div)==0:
                band=False
                break
            # Fin if
            div+=1
         # Fin while
    if band:
        print("Es primo")
    else:
        print("No es primo")
    # Fin if
else:
    print("Por favor, introduzca valor numérico")
# Fin if
# Fin Algoritmo
