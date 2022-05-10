for numero in range(1,11,3):
    print("Numero serie",numero)

contadornumero=0
for numero in range(1,21,2):
    contadornumero+=1 # Operación de incremento
    if(contadornumero<5):
        continue # Salta a la linea del for (linea 5) hasta llegar al numero deseado
    print(numero)
print("Numeros de la serie:",contadornumero)