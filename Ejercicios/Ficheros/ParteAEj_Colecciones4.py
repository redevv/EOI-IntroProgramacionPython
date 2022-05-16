from random import randint
from ParteAEj_Colecciones2 import lee_o_crea_fichero_desde_coleccion as leer_escribir

print(f"Ejecución 04:{__name__}")

ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}
for ciudad in ListaCiudades: # Recorremos la lista de ciudades
    listatemperaturas = [] # Creamos o "Reseteamos" la lista de temperaturas en cada recorrido del bucle, para que sean diferentes en cada ciudad.
    for i in range(0,12): 
        temperaturas = randint(0,50) # Generamos temperaturas comprendidas entre 0 y 50ºC
        listatemperaturas.append(temperaturas) #Almacenamos las temperaturas en una lista.
    dicc[ciudad] = listatemperaturas #Almacenamos en un diccionario el nombre de la ciudad junto a una lista con las temperaturas de enero a diciembre (12)
print(dicc)

file="./Ejercicios/Ficheros/Datos_EjCol4.txt"
leer_escribir(file,dicc)
