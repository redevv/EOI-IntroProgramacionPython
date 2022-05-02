# 12. Sumar los dígitos de un número ingresado. Ejemplo: Si se ingresa 123, debería devolver 6.

nro=input("Ingrese un nro: ")
resul=0
nro=int(nro)

while(nro!=0):
    resul=resul+(nro%10)
    nro=nro//10
# Fin while
print(f"El resultado es: {resul}")
