# 5. Construir una clase simple desde cero. Ya se ha creado una instancia para usted y los atributos de la instancia se incluyen dentro del print. 
# Tome esas pistas y con estos datos cree la clase.

#Escriba su respuesta aquí.
class Nobel():
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year 
        self.winner = winner

nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(nq2019.category, nq2019.year, nq2019.winner)
