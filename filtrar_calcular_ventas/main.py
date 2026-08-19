#El Reto: Filtrar y Calcular Métricas de Ventas
#Imagina que recibes de una tienda o de Azure Storage una lista con los registros de ventas del día.

#Tu objetivo: Escribir una función llamada procesar_ventas(ventas) que:

#Filtre únicamente las ventas cuyo estado ("estado") sea "completada" (ignora las "cancelada" o "pendiente").

#De esas ventas completadas, calcule el precio total con IVA (21%) para cada transacción (precio * 1.21).

#Devuelva una nueva lista con los IDs de las transacciones y su precio total redondeado a 2 decimales, en formato de diccionario: {"id": ..., "total": ...}.

def procesar_ventas(ventas):
    resultado = []
    for x in ventas:
        if x["estado"] == "completada":
            total_iva = round(x["precio"] * 1.21, 2)
            resultado.append({"id": x["id"],"total": total_iva})
    return resultado

# --- Probamos con los datos del ejemplo ---
ventas_diarias = [
    {"id": "TX101", "precio": 100.0, "estado": "completada"},
    {"id": "TX102", "precio": 50.0, "estado": "cancelada"},
    {"id": "TX103", "precio": 200.0, "estado": "completada"},
    {"id": "TX104", "precio": 80.0, "estado": "pendiente"}
]

print(procesar_ventas(ventas_diarias))