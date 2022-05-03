# 2. Números primos.

div=2
nro=input("Ingrese el número: ")
estado=True
if(nro.isdigit()):
    nro=int(nro)
    if (nro==1):
        print("Es primo")
    else:
        if (nro<1):
            print("ERROR!!!")
        else:
            while (nro>div):
                if (nro%div==0):
                    estado=False
                # Fin if
                div+=1
            # Fin while
        # Fin if
    if (estado==True):
        print("Es primo")
    else:
        print("No es primo")
    # Fin if
else:
    print("Por favor, introduzca valor numérico")
# Fin if
# Fin Algoritmo