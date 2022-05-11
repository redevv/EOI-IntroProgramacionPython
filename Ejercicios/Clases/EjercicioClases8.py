# 8. Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.
# Primero haga su función para que tome los parámetros: x e y. x será el número que se eleva, e y será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".
# También agreguemos una representación de cadena rápidamente, de modo que cuando un usuario imprima la clase obtenga una descripción significativa.
# Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.

#Escriba su respuesta aquí.

class Myfunc:
    def ElevarALaPotencia(x,y):
        return (y**x)
    descripcion_clase = str


ans1 = Myfunc.ElevarALaPotencia(5,6)
ans2 = Myfunc.descripcion_clase("Esta clase consistirá en operaciones matemáticas")

print(ans1)
print(ans2)