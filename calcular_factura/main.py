ventas = [
    {"id_venta": 101, "producto": "Teclado", "precio_base": 50.0},
    {"id_venta": 102, "producto": "Monitor", "precio_base": 200.0},
    {"id_venta": 103, "producto": "Ratón", "precio_base": 25.0}
]

def calcular_totales_iva(lista_ventas):
    venta = []
    for x in lista_ventas:
        total_iva = round(x["precio_base"] * 1.21, 2)
        venta.append({"id": x["id_venta"], "total_iva": total_iva})
    return venta

print(calcular_totales_iva(ventas))

