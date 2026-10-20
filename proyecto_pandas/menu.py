from cargarArchivos import cargar_archivos
from procesador import stock_correcto_valoracionok


def mostrar_menu():
    print("MENU DEL PROGRAMA")
    print("1: Cargar archivos")
    print("2: Filtrar producto")
    print("3: Salir del programa")

def iniciar_menu():
    df = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            df = cargar_archivos()
            if df is not None:
                print("Archivo cargado correctamente")
        elif opcion == "2":
            if df is not None:
                df_filtrado = stock_correcto_valoracionok(df)
                print("Registro filtrado")
                print(df_filtrado)
            else:
                print("Primero debes cargar el archivo")
        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida") 

