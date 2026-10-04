empleados = [
    {"nombre": "Ana",    "departamento": "Ventas",    "salario": 28000, "edad": 34, "activo": True},
    {"nombre": "Carlos", "departamento": "IT",        "salario": 35000, "edad": 29, "activo": True},
    {"nombre": "Laura",  "departamento": "IT",        "salario": 42000, "edad": 41, "activo": True},
    {"nombre": "Pedro",  "departamento": "Marketing", "salario": 25000, "edad": 23, "activo": False},
    {"nombre": "Marta",  "departamento": "IT",        "salario": 30000, "edad": 37, "activo": False},
    {"nombre": "Sergi",  "departamento": "Ventas",    "salario": 31000, "edad": 45, "activo": True},
    {"nombre": "Julia",  "departamento": "Marketing", "salario": 38000, "edad": 31, "activo": True},
    {"nombre": "Raúl",   "departamento": "IT",        "salario": None,  "edad": 27, "activo": True},
]

#filtrar_jovenes_activos(lista): devuelve los nombres de los empleados activos y menores de 35 años.

def filtrar_jovenes_activos(lista):
    listado = []
    for x in lista:
        if x['activo'] == True:
            if x['edad'] < 35:
                listado.append(x['nombre'])
    return listado


print(filtrar_jovenes_activos(empleados))