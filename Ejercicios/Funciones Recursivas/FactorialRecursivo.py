def Factorial(N):
    if (N<=0):
        raise # Aún no sabemos cómo funciona
    if (N<=1):
        print("return 1")
        return 1
    else:
        print("return {} Factorial({}-1)".format(N,N))
        return N*Factorial(N-1)

n=input("Calcular el factorial de (introduzca nº):")
try:
    n=int(n)
    r=Factorial(n)
    print(f"El factorial de {n} es {r}")
except TypeError:
    print("Introduzca un nº válido")
except:
    print("No se permiten valores menores a 0")