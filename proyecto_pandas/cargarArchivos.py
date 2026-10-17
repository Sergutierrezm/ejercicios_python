import pandas as pd

def cargar_archivos():
    
        try:
            df = pd.read_csv('productos.csv')
        except FileNotFoundError:
            print("No se encontró productos.csv")
            return None
        except pd.errors.EmptyDataError:
             print("El archivo productos.csv se encuentra vacio")
             return None
        print("Archivo cargado")
        return df 
