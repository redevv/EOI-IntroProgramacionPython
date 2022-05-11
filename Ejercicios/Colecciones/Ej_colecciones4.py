# Ejercicio Colecciones 4

from random import randint

NombresCiudades={"Lugo", "Pontevedra", "Gijón", "Santander", "Bilbao", "Álava", "Pamplona", "Tarragona", "Barcelona", "Castellón", "Alicante","Murcia","Albacete", "Cuenca", "Toledo", "Madrid", "Segovia", "Salamanca", "Burgos", "León"}

promedios_temperaturas=[]

for ciudad in NombresCiudades:
    for temperaturas in range(1,13):
        temperaturas=randint(-12,41)
        dict={ciudad:temperaturas}
        print(dict)

promedios_temperaturas.sort()


#print("La ciudad con menor temperatura promedio es:",promedio_tempmenor)