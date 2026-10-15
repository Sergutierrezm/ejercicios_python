#Pide dos números y muestra su suma, resta, multiplicación y división.

primer_numero = int(input("Indica el primer numero: "))
segundo_numero = int(input("Indica el segundo numero: "))

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
if segundo_numero != 0:
    division = primer_numero / segundo_numero
    print(f"la division es: {division}")
else:
    print("No se puede dividir entre o")

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"la multiplicacion es: {multiplicacion}")
