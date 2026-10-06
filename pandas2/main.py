import pandas as pd
import numpy as np

datos = {
    'producto':   ['Ratón', 'Teclado', 'Monitor', 'Portátil', 'Altavoz', 'Auriculares'],
    'categoria':  ['Accesorios', 'Accesorios', 'Informática', 'Informática', 'Audio', 'Audio'],
    'precio':     [15.5, 45.0, 189.99, 899.0, 59.0, 79.9],
    'stock':      [10, 0, 4, 2, 7, 15],
    'valoracion': [4.2, 3.8, 4.5, 4.7, 3.1, 4.0]
}

df = pd.DataFrame(datos)
print(df)


#Productos con precio mayor de 50.

mayor50 = df[df['precio'] > 50]
print(mayor50)

#productos de la categoría Audio con stock mayor de 10.

audio_stock_10 = df[(df['categoria'] == 'Audio') & (df['stock'] > 10)]
print(audio_stock_10)

#Productos que no sean de la categoría Accesorios, usando ~.

produc_no_accesorios = df[~df['categoria'].isin(['Accesorios'])]
print(produc_no_accesorios)

#Productos con precio menor de 20 o sin stock (stock igual a 0).

precioMenor20_sinStock = df[(df['precio'] < 20 ) | (df['stock'] == 0)]
print(precioMenor20_sinStock)