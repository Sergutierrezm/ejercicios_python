def analizar_temperatuas(listas):
    dia_anterior = []
    picos = []
    
    for i in range(1, len(listas) -1):
        if listas[i] > listas[i -1] and listas[i] > listas[i +1]:
            picos.append(listas[i])
    print(picos)







temperaturas = [12, 15, 14, 18, 20, 19, 16, 22, 21]
analizar_temperatuas(temperaturas)


def analizar_temperatutas(listas_des):
    picos = []
    dia_anterior = listas_des[0]
    for i in range(len(listas_des)):
        if listas_des[i] > dia_anterior:
            picos.append(listas_des[i])
        dia_anterior = listas_des[i]
    return picos

temperaturass = [12, 15, 14, 18, 20, 19, 16, 22, 21]
analizar_temperatutas(temperaturass)
print(analizar_temperatutas(temperaturass))



def detector_valles(lista_valle):
    minimos = []
    for i in range(1, len(lista_valle) - 1):
        if lista_valle[i] < lista_valle[i - 1] and lista_valle[i] < lista_valle[i +1]:
            minimos.append(lista_valle[i])
    print(minimos)
    



    return minimos
temperaturas = [20, 15, 18, 12, 10, 14, 13, 5]

detector_valles(temperaturas)