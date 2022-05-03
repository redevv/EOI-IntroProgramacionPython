# 10. Adivinar una palabra (TERMINAR)

palabra="Algoritmo"
# R=input()
estado=False
try:
    while (estado==False):
        palabraintro=input("Escriba una palabra: ")
        if (palabraintro==palabra):
            estado=True
        else:
            print("Volver a intentar(Sí/No)")
    # Fin while   
    print("¡Enhorabuena! La palabra es correcta.")
except ValueError:
    print("Por favor, introduzca sólo letras")
# Fin Algoritmo
