def Fibonacci(N):
    if (N<2):
        return N
    else:
        return Fibonacci(N-1)+Fibonacci(N-2)


n=input("Número serie Fibonacci:")
try:
    n=int(n)
    r=Fibonacci(n)
    print(f"El nº es {r}")
except TypeError:
    print("Introduzca nº válido")
except:
    print("Debe introducir un nº mayor que 0")