# 6. Construir una clase simple desde cero. Es la misma que el ejercicio anterior, ahora usará la función __str__ para devolver una representación de cadena para la clase cuando sea necesario.

#Escriba su respuesta aquí.
class Nobel():
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year 
        self.winner = winner
    def __str__(self):
        self.category = "Chemistry"
        self.year = "2019"
        self.winner = "John B. Goodenough"
         
nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(str(nq2019.category),str(nq2019.year),str(nq2019.winner))