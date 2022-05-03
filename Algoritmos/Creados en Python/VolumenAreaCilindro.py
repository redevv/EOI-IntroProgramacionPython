# 5. Volumen y Área de un Cilindro.

from math import pi
try:
    r=input("Ingrese radio del cilindro: ")
    h=input("Ingrese altura del cilindro: ")
    r=float(r)
    h=float(h)
    área=2*(pi*r*r)+2*(pi*r*h)
    volumen=pi*r**2*h
    print(f"El área del cilindro es: {área:1.2f}") # El comando N:1.2f sirve para que en el resultado se muestren solo DOS decimales.
    print(f"El volumen del cilindro es: {volumen:1.2f}")
except ValueError:
    print("Introduzca sólo valores numéricos")
# Fin Algoritmo