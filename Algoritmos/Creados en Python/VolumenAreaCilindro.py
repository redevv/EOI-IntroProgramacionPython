# 5. Volumen y Área de un Cilindro.

pi=3.14
try:
    r=input("Ingrese radio del cilindro: ")
    h=input("Ingrese altura del cilindro: ")
    r=float(r)
    h=float(h)
    área=2*(pi*r*r)+2*(pi*r*h)
    volumen=pi*r**2*h
    print(f"El área del cilindro es: {área}")
    print(f"El volumen del cilindro es: {volumen}")
except ValueError:
    print("Introduzca sólo valores numéricos")
# Fin Algoritmo