# 7. Determinar si un alumno aprueba o suspende un curso, si su media de las 3 notas es mayor o igual a 4.0

Cal1=input("Ingrese calificación 1: ")
Cal2=input("Ingrese calificación 2: ")
Cal3=input("Ingrese calificación 3: ")

try:
    Cal1=float(Cal1)
    Cal2=float(Cal2)
    Cal3=float(Cal3)
    Prom=(Cal1+Cal2+Cal3)/3

    if((Cal1>=0 and Cal1<=10) and (Cal2>=0 and Cal2<=10) and (Cal3>=0 and Cal3<=10)):
        if Prom>=4:
            print("Aprueba")
        else:
            print("Suspende")
        print(Prom)
except ValueError:
    print("Ingrese calificaciones numéricas")

