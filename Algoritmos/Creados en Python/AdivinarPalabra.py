# 10. Adivinar una palabra (CORREGIR Y TERMINAR) - Ver GitHub Cristina Silván

palabra="Algoritmo"
print("Adivina la palabra (N para Salir): ")
try:
    while True:
        palabraintro=input().lower() # .lower() facilita poner mayúsculas o minúsuculas.
        if (palabraintro==palabra):
            break
        elif (palabraintro=="N"):
            break
        print("Volver a intentar (N para Salir): ")
    print("¡Enhorabuena! La palabra es correcta.")
except ValueError:
    print("Por favor, introduzca sólo valores alfanuméricos")
# Fin Algoritmo
