precios = [12.5, 45.0, 8.0, 120.0, 3.5, 60.0]

#Escribe una función llamada filtrar_precios_altos(lista_precios)
#que devuelva una nueva lista únicamente con los precios que sean mayores a 20.0.

def filtrar_precios_Altos(lista_precios):
    lista = []
    for x in lista_precios:
        if x > 20.0:
            lista.append(x)
    return lista
    
print(filtrar_precios_Altos(precios))


