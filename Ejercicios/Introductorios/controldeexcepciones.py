numero1=100
numero2=0
try:
    print(numero1/numero2)
except ZeroDivisionError: # Opcional
    print("Error al dividir por cero")
except:
    print("otra instrucción 2")
else: # Opcional
    print("La división se calculó correctamente")
finally:
    print("Fin programa")