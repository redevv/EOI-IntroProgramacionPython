from os.path import exists

#def fichero_existe(fichero):
#    try:
#        open(fichero)
#    except FileNotFoundError:
#        return False
#    finally:
#        return True

try:
    fichero = "Ejercicios/Ficheros/ficheroprueba.txt"
    if(exists(fichero)):
        fichero=open(fichero,'rt',encoding='UTF-8')
        contenido=fichero.read()
        if(len(contenido)>0):
            print(contenido)
        else:
            print("Este fichero no tiene contenido")
    else:
        fichero=open(fichero,'wt',encoding='UTF-8')
        contenido=f"{fichero}Prueba fichero fachero"
        fichero.write(contenido)
        print("Contenido añadido")
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()