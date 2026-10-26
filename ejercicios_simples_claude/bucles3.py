#Ejercicio 1 (Para practicar while, % y saltos)
#Crea un programa con un bucle while que recorra los números del 1 al 40.

#En cada iteración, imprime el número actual por consola.

#Si el número es divisible por 5 (su resto es 0), muestra además por consola el texto: "¡Múltiplo de 5! Me salto los 2 siguientes".

#Tras imprimir ese mensaje, haz que el bucle se salte los 2 números siguientes
#  (es decir, si detecta el 5, los siguientes 2 números no se procesan y el próximo en imprimirse debería ser el 8).

i = 0
while i <= 40:
    print(i)
    if i % 5 == 0:
        print("¡Múltiplo de 5! Me salto los 2 siguientes")
        i += 3
        continue
    i +=1

#Ejercicio 2 (Para practicar for, len() y concatenación +=)
#Tienes dos listas (arrays) de strings con la misma longitud:prefijos = ['super', 'mini', 'mega']palabras = ['heroe', 'golf', 'byte']
#Crea una variable de texto (string) vacía.
#Usando un bucle for, recorre las listas y junta cada prefijo con su palabra correspondiente.
#Ve sumando el resultado a tu string vacía, añadiendo además una coma y un espacio al final de cada palabra completa.
#Al terminar el bucle, imprime la variable. El resultado final esperado por consola debe ser exactamente: "superheroe, minigolf, megabyte, "

prefijos = ['super', 'mini', 'mega']
palabras = ['heroe', 'golf', 'byte']

conjunto_palabras = " "

for i in range(len(prefijos)):
    conjunto_palabras += prefijos[i]
    conjunto_palabras += palabras[i]
    conjunto_palabras += ", "
print("Conjunto de palabras" + str(conjunto_palabras))

#Ejercicio 3 (Consolidando for, len() y concatenación +=)
#Tienes dos listas con la misma cantidad de elementos:nombres = ['Alex', 'Sara', 'Marc']apellidos = ['Gomez', 'Ruiz', 'Perez']
#Crea una variable de texto (string) vacía.
#Usando un bucle for, recorre las listas para unir cada nombre con su apellido.
#Atención al formato: Entre el nombre y el apellido debes añadir un espacio en blanco (" "). Además, después del apellido, debes añadir un guion con espacios (" - ") para separar a cada persona.
#Imprime la variable una única vez al terminar el bucle.
#El resultado esperado por consola debe ser exactamente este:"Alex Gomez - Sara Ruiz - Marc Perez - "

nombres = ['Alex', 'Sara', 'Marc']
apellidos = ['Gomez', 'Ruiz', 'Perez']

conjunto_nombres = " "

for i in range(len(nombres)):
    conjunto_nombres += nombres[i]
    conjunto_nombres += " "
    conjunto_nombres += apellidos[i]
    conjunto_nombres += " - "
print("Nombres completos: " + str(conjunto_nombres))



#Ejercicio 5 (Descifrando un mensaje oculto)
#Tienes dos arrays. Uno contiene letras desordenadas y el otro contiene los números que indican el orden correcto en el que hay que leerlas:letras = ['o', 'a', 'h', '!', 'l']orden = [2, 0, 4, 1, 3]
#Crea una variable de texto (string) vacía llamada mensaje.
#Usando un bucle for, recorre el array orden.
#En cada vuelta, usa el valor numérico que te da orden para acceder a la posición correspondiente en el array letras.
#Suma (concatena) esa letra a tu variable mensaje.
#Al terminar el bucle, imprime mensaje una sola vez.


letras = ['o', 'a', 'h', '!', 'l']
orden = [2, 0, 4, 1, 3]

mensaje = " "

for i in range(len(orden)):
    mensaje += letras[orden[i]]
print("El mensaje es: "  + str(mensaje))


carnes = ['Entrecot', 'Chuletón', 'Secreto ibérico']
puntos = ['Poco hecho', 'Al punto', 'Muy hecho']

for carne in carnes:
    for punto in puntos:
        if carne == carnes[2] and punto == puntos[0]:
            continue
        print("Marchando" + " - " +str(carne) +  " " + str(punto))

