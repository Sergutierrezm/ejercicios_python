#Tu objetivo:
#Escribe un script en Python que recorra la lista registros y devuelva un diccionario con el recuento total de accesos por cada usuario.


temperaturas = [18, 25, 31, 15, 29, 34, 22]

def filtrado_temperaturas(datos):
    datos_moderadas = []
    datos_calurosas = []

    for x in datos:
        if x > 25:
            datos_calurosas.append(x)
        else:
           datos_moderadas.append(x)
    return datos_moderadas, datos_calurosas     


print(filtrado_temperaturas(temperaturas))