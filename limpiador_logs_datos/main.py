#Enunciado: Limpiador y Transformador de Logs de Datos
#Objetivo:

#Crea una función llamada filtrar_y_duplicar_pares(datos) que reciba una lista heterogénea de datos y devuelva una nueva lista procesada.

#Requisitos:

#Filtrar la lista original para conservar únicamente los números enteros (int). Hay que ignorar cadenas, flotantes, None y booleanos (True/False).

#De los enteros filtrados, seleccionar solo los que sean números pares.

#Devolver una nueva lista donde cada uno de esos números pares aparezca multiplicado por 2.

def filtrar_y_duplicar_pares(datos):
    resultado = []
    for x in datos:
        if type(x) == int:
            if x % 2 == 0:
                resultado.append(x * 2)
    return resultado
entrada = [1, 4, "error", 10, 3.14, True, 7, 8, None]
print(filtrar_y_duplicar_pares(entrada))