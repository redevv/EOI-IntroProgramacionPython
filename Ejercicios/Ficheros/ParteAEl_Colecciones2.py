from random import randint
from os.path import exists

def lee_o_crea_fichero_desde_coleccion(file_nombre,lista_datos):
    try:
        if(exists(file_nombre)):
            fichero=open(file_nombre,'rt',encoding='UTF-8')
            contenido=fichero.read()
            print(f"El contenido del fichero previamente creado es:\n{contenido}")
        else:
            fichero=open(file_nombre,'wt',encoding='UTF-8')
            fichero.write(str(lista_datos))
            print(f"Fichero {file}: generado")
    except Exception as e:
        print(f"E:{e}")
    finally:
        fichero.close()

print(f"Ejecución {__name__}")
if __name__ == '__main__': # Con este comando hacemos que sólo se ejecute la función de arriba en otro programa para evitar duplcaciones
    personas=[]
    for n in range(1,101):
        personas.append(randint(0,125))

    personas1 = [randint(0,125) for i in range(1,101)] # equivale a las lineas 3, 4 y 5

    file = "./Ejercicios/Ficheros/Datos_EjCol2.txt"
    file1 = "./Ejercicios/Ficheros/Datos_EjCol2A.txt"

    lee_o_crea_fichero_desde_coleccion(file,personas)
    lee_o_crea_fichero_desde_coleccion(file1,personas1)



