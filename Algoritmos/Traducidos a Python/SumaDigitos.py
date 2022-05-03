# 12. Sumar los dígitos de un número ingresado. Ejemplo: Si se ingresa 123, debería devolver 6.

nro=input("Ingrese un nro: ")
if (nro.isdigit()):
    nro=int(nro)    
    resul=0
    while(nro!=0):
        resul=resul+(nro%10)
        nro=nro//10
    # Fin while
    print(f"El resultado es: {resul}")
else:
    print("Por favor, introduzca un número válido")
# Fin Algoritmo
