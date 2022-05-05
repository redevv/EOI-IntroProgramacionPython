import json
jsonventas='{"departamento": 8,"nombredepto": "Ventas","director": "Juan Rodriguez","empleados": [{"nombre": "Pedro","apellido": "Fernandez"},{"nombre": "Jacinto","apellido": "Benavente"}]}'
print(jsonventas)
datosDepto=json.dumps(jsonventas)
print(type(datosDepto))
print("JSON Depto:",datosDepto)
jsonventas=json.loads(datosDepto)
print(type(datosDepto))

for val in jsonventas:
    print(val,jsonventas[val])
