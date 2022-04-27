contadornumero=0
for numero in range(1,21,2):
    contadornumero+=1 # Operación de incremento
    if(contadornumero>5):
        break # Salta a la linea después del bloque for (sale del for)
    print(numero)
print("Numeros de la serie:",contadornumero)