# Ejercicio Colecciones 4

from random import randint

NombresCiudades={"Lugo", "Pontevedra", "Gijón", "Santander", "Bilbao", "Álava", "Pamplona", "Tarragona", "Barcelona", "Castellón", "Alicante","Murcia","Albacete", "Cuenca", "Toledo", "Madrid", "Segovia", "Salamanca", "Burgos", "León"}

dicc={}

for ciudad in NombresCiudades:
    for temperaturas in range(1,13):
        temperaturas=randint(-10,49)

