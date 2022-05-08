# -*- coding: utf-8 -*-
'''
Debe completar las dos líneas de código faltantes de este script.
NO SE PERMITE:
 1- Crear más líneas de código.
 2- Crear o usar funciones (NINGUNA) 
 3- Usar diccionarios
 4- Usar el punto y coma.
 5- Recomiendo no usar ningún tipo de información aparte de la que está en este script, aunque se puede usar Google,
 este script contienen información más que suficiente para resolver el reto...

El usuario deberá ingresas desde la consola, terminal un año desde cero a cualquier año positivo y el programa le mostrará
el signo del horóscopo chino al cual pertenece ese año

Estos son los signos del horóscopo chino desde el año cero hasta el año doce:
Año 0: "Mono"
Año 1: "Gallo"
Año 2: "Perro"
Año 3: "Cerdo"
Año 4: "Rata"
Año 5: "Buey"
Año 6: "Tigre"
Año 7: "Conejo"
Año 8: "Dragón"
Año 9: "Serpiente"
Año 10: "Caballo"
Año 11: "Cabra"
Año 12: "Mono"

Resultados esperados: 
1978: "Caballo"
1990: "Caballo"
2000: "Dragón"
2020: "Rata"
2022: "Perro"
5301: "Serpiente"

'''
try:
    while True:
       año=int(input('Debe ingresar el año y se le dirá a qué signo del horóscopo chino pertenece\n¡No debe ingresar años negativos!: '))
       if año < 0:
            año_error=ValueError("No se permiten años Antes de Cristo")
            raise año_error
       # Complete la primera línea de código
       # Cree la variable resultado para completar la segunda línea de código
       print(resultado)
except:
    if "año_error" in locals():
        print(año_error)
    else:
        print("Usted ha ingresado un valor inválido")
