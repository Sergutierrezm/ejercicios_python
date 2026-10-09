import pandas as pd

def cargar_archivos():
    print("Procesando archivo")
    df = pd.read_csv('productos.csv')
    return df 
