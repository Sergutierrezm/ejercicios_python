#Tu objetivo:Escribe una función llamada limpiar_nombres(lista) que recorra la lista y devuelva una nueva lista con los nombres:
# Sin espacios en blanco a los lados.Con la primera letra en mayúscula y el resto en minúscula (ejemplo: "  sergio " $\rightarrow$ "Sergio").
def limpiar_nombres(lista):
    listado = []

    for usuario in lista:
        nombre_limpio = usuario.strip().capitalize()
        listado.append(nombre_limpio)
    return listado    
    

usuarios_raw = ["  sergio ", "ALBA", " carlos", "  Marta  "]

print(limpiar_nombres(usuarios_raw))


       
            