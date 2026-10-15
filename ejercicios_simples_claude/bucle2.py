#Imprime la tabla de multiplicar del número que elija el usuario.

numero = int(input("indica un numero"))

for i in range(1,11):
   print(f"{numero} x {i} = {numero * i}")