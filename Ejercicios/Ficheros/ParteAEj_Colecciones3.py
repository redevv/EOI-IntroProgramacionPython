from random import randint
from ParteAEj_Colecciones2 import lee_o_crea_fichero_desde_coleccion as leer_escribir

print(f"Ejecución 03:{__name__}")

mujeres=[]
hombres=[]

#for n in range(1,101):
#    genero=randint(0,1)
#    if (genero==1):
#        mujeres.append(randint(0,101))
#    else:
#        hombres.append(randint(0,101))
genero=[randint(0,1) for n in range(1,101)] 
mujeres=[randint(0,101) for g in genero if g==1]
hombres=[randint(0,101) for g in genero if g==0]

fileChicos="./Ejercicios/Ficheros/DatosChicos_EjCol3.txt"
fileChicas="./Ejercicios/Ficheros/DatosChicas_EjCol3.txt"

leer_escribir(fileChicas,mujeres)
leer_escribir(fileChicos,hombres)
