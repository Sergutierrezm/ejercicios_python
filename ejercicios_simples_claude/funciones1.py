def analizar_texto(texto, caracter):
    if texto is None:
        print("Error: No hay datos")
    else:
        texto_limpio = texto.strip().upper()
        print(f"El texto tiene {len(texto_limpio)} caracteres y la letra esta en la posicion {texto_limpio.find(caracter)}")
        
    return



analizar_texto("   analitica de datos   ", "D")
analizar_texto(None, "A")

print("\n-------------")

def validar_password(password):
    if password is None:
        return("Error: sin contraseña")
    else:
        contraseña_limpia = password.strip()
        
        if len(contraseña_limpia) < 8:
            return("Contraseña muy corta")
        else:
            return("Contraseña valida")
    
    
print(validar_password(None))
print(validar_password("   12345   "))
print(validar_password("   MiClaveSecreta "))


print("\n----------")

def limpiar_usuario(nombre):
    if nombre is None:
        print("Invitado")
    else:
        nombre_limpio = nombre.strip().lower()
        return nombre_limpio
    return
    

limpiar_usuario("    SERGIO")


