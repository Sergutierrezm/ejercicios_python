def procesar_registros(datos):
    resultado = []
    for x in datos:
        if not x["activo"]:
            continue
        usuario_limpio = x["usuario"].strip().lower()
        email_raw = x["email"].lower()
        email_limpio = None if email_raw == "invalido" else email_raw

        edad_limpia = int(x["edad"]) if x["edad"] is not None else None

        registro_limpio = {
            "usuario": usuario_limpio,
            "email": email_limpio,
            "edad": edad_limpia,
            "activo": x["activo"]
        }

        resultado.append(registro_limpio)
    return resultado    

registros_raw = [
    {"usuario": "  juan_perez ", "email": "JUAN@gmail.com", "edad": "28", "activo": True},
    {"usuario": "maria_gomez", "email": "maria@hotmail.com", "edad": None, "activo": True},
    {"usuario": "CARLOS_LOPEZ", "email": "carlos_lopez@yahoo.es", "edad": "35", "activo": False},
    {"usuario": "ana_soto  ", "email": "INVALIDO", "edad": "22", "activo": True},
]

registros_limpios = procesar_registros(registros_raw)
print(registros_limpios)
