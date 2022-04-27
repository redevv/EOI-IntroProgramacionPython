from datetime import datetime # De todo el modulo (from) importar (import) solo lo que necesito

datenow1=datetime.now().date() # Muestra solo la fecha
print("Fecha: ",datenow1)
print("Año fecha1:",datenow1.year)
print("Mes fecha1:",datenow1.month)
print("Dia fecha1:",datenow1.day)
# print("Hora fecha1:",datenow1.hour) -> NO esta disponible porque la variable solo contiene la fecha

datenow2=datetime.now() # Muestra fecha y hora exactas
print("Fecha: ",datenow2)
print("Año fecha2:",datenow2.year)
print("Mes fecha2:",datenow2.month)
print("Dia fecha2:",datenow2.day)
print("Hora fecha2",datenow2.hour)
print("Minuto fecha2",datenow2.minute)
print("Segundo fecha2",datenow2.second)
print("Microsegundo fecha2",datenow2.microsecond)