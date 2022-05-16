from random import randint
#from Colecciones.Ej_Col1Alvaro import ClasificaGenero

personas=[]
for n in range(1,101):
    genero=randint(0,1) #0 para chicas y el 1 los chicos
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
print(f"Lista de personas:{personas}")

from os.path import exists

try:
    file="./Ejercicios/Ficheros/Datos_EjCol1.txt"
    if(exists(file)):
        print("Fichero previamente generado no se sobreescribe")
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        print(f"El contenido del fichero es: \n{contenido}")
    else:
        fichero=open(file,'wt',encoding='UTF-8')
        fichero.write((str(personas)))
except Exception as e:
    print(f"E:{e}")
finally:
    fichero.close()
