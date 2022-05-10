# 4. Agregue otro atributo llamado "cantidad" al método de inicialización (generalmente denominado constructor o init).
#Luego defina "asignar" este atributo al atributo self.quantity dentro del constructor.
#Luego cree 2 instancias para: F14 y Mirage2000 con cantidades 87 y 35.

class Jets:
    model = None
    country = 0
    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity

#Escriba su respuesta aquí.        
first_item=Jets("F14", "USA",87)
second_item=Jets("Mirage2000", "France",35)
total=first_item.quantity+second_item.quantity
print(total)