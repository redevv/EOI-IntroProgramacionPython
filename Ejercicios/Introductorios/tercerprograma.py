from re import U


ciudad="madrid"
print(ciudad.isdigit())

minombre="david"
print(len(minombre)) # Muestra numero caracteres variable

print(minombre[2]) # Muestra posicion original
print(minombre[0])
# print(minombre[5]) String index out of range

print(minombre[:4]) # Muestra numero caracteres siguientes al inicial 
print(minombre[3:]) # Viceversa del anterior
print(minombre[1:4]) # Muestra caracteres entre dichos numeros
print(minombre[-3]) # Muestra posicion desde el final

mensaje="dd"
print("hola {}" .format(mensaje))
# print("hola "+mensaje) -> NO es una forma eficiente de concatenar cadenas de caracteres
ciudad="albacete"
print("hola {m} de {c}" .format(m=mensaje, c=ciudad))

numero=10/3
print("El numero sin formato es {}" .format(numero)) # Muestra TODO el contenido del numero
print("El numero con formato es {n:1.2f}" .format(n=numero)) # Muestra solo dos decimales

print(f"Hola {mensaje} de {ciudad}") # Forma mas eficiente de dar formato