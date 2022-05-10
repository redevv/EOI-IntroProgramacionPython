# Ejercicios de colecciones (algoritmos)

1. Hacer un programa que procese 100 mujeres y hombres (M/H). Mostrar el porcentaje de hombres y mujeres y si hay más mujeres que hombres, si hay igualdad o si hay más hombres que mujeres.

```
Ejercicio CienHombresyMujeres (hecho por Billy)
	Entrada
		Leer DatosPersona 1 a 1
		Generamos esos datos 
			Generacion aleatoria
			     0 = chicas
			     1 = chicos
    Proceso	Algoritmo	     
		Asignamos esa generacion a una colección
        Preguntar por las chicas (Cuantas son)
        Preguntar por los Chicos
        Preguntar si hay mas chicas que chicos
        Preguntar si hay mas chicos que chicas
        Preguntar si hay igualdad
    Salida Algoritmo
        Escribir El resultado de las chicas
        Escribir El resultado de las chicos
        Si hay mas chicas que chicos
        o mas chicos que chicas
        o hay igualdad
FinAlgoritmo
```

2. Hacer un programa que procese las edades de 100 personas. Deberá decir cuantas tienen más de (≥18) y cuál es la persona con menor edad y cuál es la persona con mayor edad. También deberá mostrar el porcentaje de edades de las 100 personas.

```
Ejercicio EdadesCienPersonas
    Entrada Algoritmo
        Leer Edades de las 100 personas
            Generar Edades de manera aleatoria de 0 a 100 años
    Proceso Algoritmo
        Preguntar Edades>=18
        Clasificar Edades para contar repeticiones
        Preguntar Menor Edad
        Preguntar Mayor Edad
    Salida Algoritmo
        Escribir Edades>=18
        Escribir Persona Menor Edad
        Escribir Persona Mayor Edad
        Recorrer Lista y Escribir Porcentaje Edades
Fin Algoritmo
```

3. Hacer un programa que procese un total de 100 personas y establecer cuantas son mujeres mayores de edad y cuantos hombres menores de edad. Deberá sacar el hombre y la mujer con menor edad, el hombre y la mujer con mayor edad, promedio de edades de las mujeres y promedio de edades de los hombres.

````
Ejercicio EdadesyPromedios
    Entrada Algoritmo
        Leer Datos 100 personas
            Generar Datos 100 personas de manera aleatoria
            h=hombres
            m=mujeres
                Generar Edades para esas 100 personas
    Proceso Algoritmo
        Preguntar mujeres >=18
        Preguntar hombres <18
        Preguntar h y m con menor edad
        Preguntar h y m con mayor edad
    Salida Algoritmo
        Escribir mujeres >=18
        Escribir hombres <18
        Escribir h y m con menor edad
        Escribir h y m con mayor edad
        Recorrer lista y escribir promedio edades h y m
Fin Algoritmo
````

4. Hacer un programa que procese las temperaturas mensuales de 20 ciudades. Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y cual la más baja. También deberá sacar la lista de las 20 ciudades con el promedio de temperaturas anuales desde la más alta hasta la más baja.

````
Ejercicio TemperaturasMensuales
    Entrada Algoritmo
        Leer datos 20 ciudades
            Generar temperatura por cada mes a cada ciudad
    Proceso Algoritmo
        Asignar generación a un diccionario
        Preguntar Ciudad con temperatura promedio más alta
        Preguntar Ciudad con temperatura promedio más baja
    Salida Algoritmo
        Escribir Ciudad con temperatura promedio más alta
        Escribir Ciudad con temperatura promedio más baja
        Escribir lista ordenada de las 20 ciudades con temperatura promedio desde más alta hasta más baja
Fin Algoritmo
````


