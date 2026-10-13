categorias = ["Periféricos", "Audio", "Periféricos", "Pantallas", "Periféricos", "Audio"]

#Escribe un script o función que recorra esa lista 
#y cree un diccionario con el conteo total de productos por categoría.



def categorizar_lista(lista):
    datos = {}
    for x in lista:
        if x in datos:
            datos[x] += 1
        else:
            datos[x] = 1
    return datos
    
print(categorizar_lista(categorias))    