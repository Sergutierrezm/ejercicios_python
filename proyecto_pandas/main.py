import pandas as pd
from procesador import stock_correcto_valoracionok

def main():
    df = pd.read_csv("productos.csv")

    df_filtrado = stock_correcto_valoracionok(df)

    print("---Productos cargados desde el CSV---")
    print(df_filtrado)



if __name__ == "__main__":
    main()
