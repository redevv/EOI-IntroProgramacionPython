# 8. Factorial de cualquier número -> CORREGIR (Ver GitHub Antonio Daza)

nro=input("Ingrese número: ")
m=2
resul=0
nro=int(nro)
if (nro==1):
    print(1)
else:
    while (m<=nro):
        resul=resul*m
        m+=1
    # Fin while
    print("El factorial es",resul)
# Fin if
# Fin Algoritmo