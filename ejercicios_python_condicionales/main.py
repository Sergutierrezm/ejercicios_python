#1. Año bisiesto y estación
#Dado un año y un mes (1-12), indica si el año es bisiesto y cuántos días tiene ese mes. Además,
# muestra la estación del hemisferio norte a la que pertenece el mes (diciembre, enero y febrero son invierno, y así sucesivamente).

año = 2024
mes = 4

es_bisiesto = año % 4 == 0


if mes < 1 or mes > 12:
    print("Mes no valido")
else:
    if es_bisiesto:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dias = 31
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias = 30
            if mes == 12 or mes == 1 or mes == 2:
                estacion = "invierno"
                print(f"Es bisiesto y el mes es: {mes} y tiene {dias} dias y la estacion es {estacion} ")
            elif mes >= 3 and mes <= 5:
                estacion = "primavera"
                print(f"Es bisiesto y el mes es: {mes} y tiene {dias} dias y la estacion es {estacion} ")
        else: 
            if es_bisiesto and mes == 2:
                dias = 29
            else:
                dias = 28
            print("Es bisiesto")
    
    else:
        print("No es bisiesto")







