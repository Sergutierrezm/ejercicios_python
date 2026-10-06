#escribe limpiar_productos(lista) que reciba una lista de diccionarios y devuelva una lista nueva con estas reglas:

#Descarta los productos con activo en False.
#producto: quita espacios sobrantes y pasa a minúsculas.
#precio: llega como texto con coma decimal ("15,50"), conviértelo a número (float). Si es None, déjalo en None.
#stock: si es None, ponlo a 0.
#El diccionario de salida solo lleva producto, precio y stock.

productos_raw = [
    {"producto": "  Ratón ", "precio": "15,50",  "stock": 10,   "activo": True},
    {"producto": "TECLADO",  "precio": "45",     "stock": None, "activo": True},
    {"producto": "Monitor ", "precio": "189,99", "stock": 4,    "activo": False},
    {"producto": " Altavoz", "precio": None,     "stock": 7,    "activo": True},
]

def limpiar_productos(lista):
    datos = []
    for x in lista:
        if x['activo'] == True:
            producto_limpio = x['producto'].strip().lower()
            precio_limpio = float(x['precio'].replace(',','.')) if x['precio'] is not None else None
            stock_limpio = x['stock'] if x['stock'] is not None else 0

            registro_limpio = {
                "producto": producto_limpio,
                "precio": precio_limpio,
                "stock": stock_limpio
                
            }
            datos.append(registro_limpio)
    return datos


registros_limpios = limpiar_productos(productos_raw)
print(registros_limpios)        

productos_raw = [
    {"producto": "  Ratón ", "precio": "15,50",  "stock": 10,   "activo": True},
    {"producto": "TECLADO",  "precio": "45",     "stock": None, "activo": True},
    {"producto": "Monitor ", "precio": "189,99", "stock": 4,    "activo": False},
    {"producto": " Altavoz", "precio": None,     "stock": 7,    "activo": True},
]