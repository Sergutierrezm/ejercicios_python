from cargarArchivos import cargar_archivos
from procesador import stock_correcto_valoracionok
from loader import cargar_a_postgres

def mostrar_menu():
    print("\n--- MENU DEL PROGRAMA (ETL) ---")
    print("1: Cargar archivos (Extract)")
    print("2: Filtrar producto (Transform)")
    print("3: Guardar en Base de Datos (Load)")
    print("4: Salir del programa")

def iniciar_menu():
    df = None
    df_filtrado = None
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            df = cargar_archivos()
            if df is not None:
                print("Archivo cargado correctamente.")
                
        elif opcion == "2":
            if df is not None:
                df_filtrado = stock_correcto_valoracionok(df)
                print(f"Registros filtrados correctamente: {len(df_filtrado)} filas.")
                print(df_filtrado)
            else:
                print("Error: Primero debes cargar el archivo (Opción 1).")
                
        elif opcion == "3":
            if df_filtrado is not None:
                # 'productos_destacados' será el nombre de la tabla en tu PostgreSQL
                exito = cargar_a_postgres(df_filtrado, "productos_destacados")
                if exito:
                    print("Ciclo ETL completado.")
            else:
                print("Error: Primero debes filtrar los datos (Opción 2).")
                
        elif opcion == "4":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opcion no valida. Por favor, elige un número del 1 al 4.")

