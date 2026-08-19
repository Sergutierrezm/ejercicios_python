#Tu objetivo:
#Escribe una función llamada filtrar_it_altos(lista) que devuelva una lista con los nombres de los empleados que cumplan dos condiciones:
#Pertenecer al departamento "IT".
#Tener un salario mayor a 30.000.

def filtrar_it_altos(lista):
    listado = []
    for x in lista:
        if x["departamento"] == "IT":
            if x["salario"] > 30000:
                listado.append(x["nombre"])
    return listado


empleados = [
    {"nombre": "Ana", "departamento": "Ventas", "salario": 28000},
    {"nombre": "Carlos", "departamento": "IT", "salario": 35000},
    {"nombre": "Laura", "departamento": "IT", "salario": 42000},
    {"nombre": "Pedro", "departamento": "Marketing", "salario": 25000}
]

print (filtrar_it_altos(empleados))            
