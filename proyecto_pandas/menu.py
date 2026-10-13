from cargarArchivos import cargar_archivos
from procesador import stock_correcto_valoracionok


def mostrar_menu():
    print("MENU DEL PROGRAMA")
    print("Cargar archivos")

def iniciar_menu():
    opciones = {
        "1": cargar_archivos,
        "2": stock_correcto_valoracionok
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
            if df is not None:
                stock_correcto_valoracionok(df)
        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida") 

