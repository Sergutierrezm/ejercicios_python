from cargarArchivos import cargar_archivos
def mostrar_menu():
    print("MENU DEL PROGRAMA")
    print("Cargar archivos")

def iniciar_menu():
    opciones = {
        "1": cargar_archivos
    }

    df = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion").strip()

        if opcion in opciones:
            resultado = opciones[opcion]()
            if resultado is not None:
                df = resultado
        elif opcion == "2":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida") 

