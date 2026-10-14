from cargarArchivos import cargar_archivos
from procesador import stock_correcto_valoracionok


def mostrar_menu():
    print("MENU DEL PROGRAMA")
    print("Cargar archivos")

def iniciar_menu():
    

    df = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion").strip()

        if opcion == "1":
            df = cargar_archivos()
            if df is not None:
                print("Archivo cargado correctamente")
        elif opcion == "2":
            if df is not None:
                df_filtrado = stock_correcto_valoracionok(df)
                print("Registro filtrado")
                print(df_filtrado)
        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida") 

