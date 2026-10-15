#Pide al usuario su nombre y su año de nacimiento,
#y muestra un mensaje del tipo Hola Ana, este año cumples X años.

nombre = input("Indica tu nombre: ")
año = int(input("Indica tu año de nacimiento: "))

edad = 2026 - año


print(f"Hola {nombre}, este año cumples {edad}")