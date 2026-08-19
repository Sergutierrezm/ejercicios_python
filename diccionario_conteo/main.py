
registros = ["Juan", "María", "Juan", "Carlos", "María", "Ana", "Juan"]
def procesar_conteo(datos):
    conteo = {}
    for usuario in datos:
        if usuario in conteo:
            conteo[usuario] +=1
        else:
            conteo[usuario] = 1
    return conteo


print(procesar_conteo(registros))
    