# 5. Sumar todos los números pares entre 2 y 100.

suma=0
nro=2
while (nro<=100):
    if (nro%2==0):
        suma=suma+nro # Otra forma: suma+=nro
    # Fin if
    nro=nro+1 # Así es más claro, otra opción: nro+=1
# Fin while
print(f"La suma de los pares entre nro y 100 es: {suma}")
# Fin Algoritmo