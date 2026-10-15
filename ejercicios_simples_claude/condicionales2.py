#Pide una nota del 0 al 10 y muestra: Suspenso (<5), 
# Aprobado (5-6.9), Notable (7-8.9) o Sobresaliente (9-10).

nota = float(input("Indica la nota que sacaste: "))

if nota < 0 or nota > 10:
    print("La nota tiene que ser de 0 a 10")
elif nota < 5:
    print(f"Tu nota es {nota} y estas suspenso")
elif nota <= 6.9:
    print(f"Tu nota es {nota} y estas aprobado")
elif nota <= 8.9:
    print(f"Tu nota es {nota} y tienes un notable")
else:
    print(f"Tu nota es {nota} y tienes un sobresaliente")  
