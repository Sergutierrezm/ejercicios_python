import pandas as pd




def stock_correcto_valoracionok(df):
    stock0_valoracion3 = df[(df['stock'] > 0) & (df['valoracion'] > 3)]
    return stock0_valoracion3



