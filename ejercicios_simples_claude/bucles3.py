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



#Ejercicio 4 (Descifrando un mensaje oculto)
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


#Ejercicio 5 (Menú de carnes con restricciones)
#Tienes dos listas para organizar las combinaciones posibles en una barbacoa:
#carnes = ['Entrecot', 'Chuletón', 'Secreto ibérico']
#puntos = ['Poco hecho', 'Al punto', 'Muy hecho']
#Utiliza dos bucles for anidados para combinar cada tipo de carne con cada punto de cocción.
#En cada iteración, imprime el resultado exactamente con este formato: "Marchando: [carne] - [punto]".
#El reto adicional: El cerdo requiere mayor temperatura por seguridad. Añade una condición if dentro del bucle anidado para que, si la carne es "Secreto ibérico" y el punto es "Poco hecho", el programa se salte esa iteración específica (usando continue) y no la imprima.
#Al ejecutarlo, la consola debería mostrar el Entrecot y el Chuletón en los tres puntos de cocción, pero el Secreto ibérico solo aparecerá en las versiones "Al punto" y "Muy hecho", sumando un total de 8 combinaciones en lugar de 9.

carnes = ['Entrecot', 'Chuletón', 'Secreto ibérico']
puntos = ['Poco hecho', 'Al punto', 'Muy hecho']

for carne in carnes:
    for punto in puntos:
        if carne == carnes[2] and punto == puntos[0]:
            continue
        print("Marchando" + " - " +str(carne) +  " " + str(punto))

#Ejercicio 6
# Crear un array de números enteros variados (puedes usar el del ejemplo de abajo).
# Crear una variable entera llamada "puntuacion" iniciada a 0.
# Recorrer el array sumando cada número a la variable "puntuacion".
# Regla 1: Si el número que toca sumar es un 7, saltarlo (no sumarlo) y pasar al siguiente.
# Regla 2: Si el número que toca sumar es un -1, detener el bucle por completo (game over).
# Regla 3: Comprobar la puntuación justo DESPUÉS de hacer la suma. Si es mayor o igual a 50, detener el bucle (victoria).
# Si el bucle no ha saltado ni se ha detenido, imprimir en esa vuelta: "Puntos hasta ahora: [puntuacion]".

print("\n\nEJERCICIO 7")

valores = [15, 20, 7, 10, 8, -1, 5]
puntuacion = 0

# Escribe tu bucle a partir de aquí

for i in valores:
    if i == 7:
        continue
    if i == -1:
        break

    puntuacion += i
    
    if puntuacion >= 50:
        print("Victoria")
        break

   
        
    print("Puntos hasta ahora: " + str(puntuacion))




#Esta técnica de enfrentar dos punteros es ideal para modificar un array sin tener que crear uno nuevo. El reto ahora es invertir el orden de los elementos intercambiando sus posiciones.
#Instrucciones:
#Tienes una lista de letras que forman una palabra al revés.letras = ['a', 'c', 'i', 'g', 'o', 'l']
#Crea los dos punteros (i apuntando al índice 0, y j apuntando al último índice usando len()).
#Crea un bucle while que se ejecute mientras el puntero izquierdo no cruce al derecho (i < j).
#Dentro del bucle, intercambia el valor de la posición i con el de la posición j.(Pista universal de programación: para no perder un valor al sobrescribirlo, guárdalo primero en una variable temporal, por ejemplo: aux = letras[i])
#Avanza el puntero i sumándole 1, y retrocede el puntero j restándole 1.
#Fuera del bucle, imprime el array letras entero. Si lo has hecho bien, debería mostrar ['l', 'o', 'g', 'i', 'c', 'a'].

print("\n\nEJERCICIO 8")

letras = ['a', 'c', 'i', 'g', 'o', 'l']

i = 0

j = len(letras) -1

# Escribe tu bucle while a partir de aquí

while i < j:

    aux = letras[i]

    letras[i] = letras[j]
    letras[j]= aux
   
    i += 1
    j -=1
print(letras)

#Ejercicio 9 (Contando butacas de cine)

#Tienes esta matriz que representa las butacas de una pequeña sala de cine. Un 0 significa que el asiento está libre, y un 1 que está ocupado:
#Tu misión:
#Usando dos bucles for (uno dentro de otro), recorre toda la matriz. Cada vez que encuentres un 1, súmale 1 a la variable asientos_ocupados. Al final del todo, imprime cuántos asientos están ocupados (debería darte 5).
print("\n\nEJERCICIO 9")

cine = [
    [0, 0, 1],
    [1, 1, 1],
    [0, 1, 0]
]

asientos_ocupados = 0

for i in cine:
    for j in i:

        if j == 1:
            asientos_ocupados += 1
print(asientos_ocupados)





print("\n\nEJERCICIO 10")

flexiones = [
    [10, 10, 10, 8],  # Día 1
    [12, 12, 10, 10], # Día 2
    [15, 12, 12, 10]  # Día 3
]

series_top = 0

for i in flexiones:
    for j in i:
        if j >= 12:
            series_top += 1
print(series_top)