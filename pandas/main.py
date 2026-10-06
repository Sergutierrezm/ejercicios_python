#Estudiantes con puntuación mayor de 80.
#Estudiantes mayores de 21 o con puntuación menor de 50 (|).
#Estudiantes que no hayan aprobado, usando ~.
#Solo las columnas nombre y puntuacion de los aprobados.
#Estudiantes cuyo nombre esté en ['Ana', 'Elena', 'Jorge'] (isin).
#Los aprobados ordenados por puntuación de mayor a menor (sort_values).
#Cuántos estudiantes aprobados son menores de 22 (len(...)).
#Estudiantes con edad entre 20 y 23, ambos incluidos (between).
#La puntuación media de los estudiantes de 22 años o más (.mean()).
#Una columna nueva aprobado con True/False y luego filtra usando solo esa columna.

import pandas as pd

# Creamos un DataFrame de ejemplo
datos = {
    'nombre': ['Ana', 'Carlos', 'Elena', 'David', 'Lucía', 'Jorge'],
    'edad': [22, 19, 25, 21, 23, 18],
    'puntuacion': [85, 62, 45, 78, 92, 55]
}

df = pd.DataFrame(datos)
print(df)


#Estudiantes con puntuación mayor de 80.
estudiantes_80 = df[df['puntuacion'] > 80]

print(estudiantes_80)


#Estudiantes mayores de 21 o con puntuación menor de 50 (|).

estudiantes21_50 = df[(df['edad'] > 21 ) | (df['puntuacion'] < 50)] 
print(estudiantes21_50)

#Estudiantes que no hayan aprobado, usando

estu_noaprobados = df[~(df['puntuacion'] >= 50)]
print(estu_noaprobados)

#Solo las columnas nombre y puntuacion de los aprobados.

nombre_puntu_apro = df[df['puntuacion'] >= 50]  [['nombre', 'puntuacion']]
print(nombre_puntu_apro)

#Filtra los estudiantes que tengan 20 años o más Y que además hayan obtenido una puntuación mayor o igual a 75.

estu20_mayor75 = df[(df['edad'] >= 20 ) & (df['puntuacion'] >= 75 )]
print(estu20_mayor75)

#Obtén un nuevo DataFrame con los estudiantes cuyos nombres NO sean 'Carlos' ni 'Jorge'.
estu_no_jorge_carlos = df[~df["nombre"].isin(['Carlos', 'Jorge'])]
print(estu_no_jorge_carlos)

#Añade una columna llamada 'estado' al DataFrame original:
#'Aprobado' si la puntuación es mayor o igual a 60.
#'Suspenso' si la puntuación es menor a 60.

import numpy as np
df['estado'] = np.where(df['puntuacion'] >=60, 'aprobado', 'suspenso')
print(df)

#Encuentra a los estudiantes que tengan una edad entre 19 y 22 años (ambos inclusive) utilizando el método

entre19_22 = df[df['edad'].between(19,22)]
print(entre19_22)

#Sube 5 puntos de puntuación exclusivamente a aquellos estudiantes que hayan obtenido una puntuación menor a 60

df.loc[df['puntuacion'] < 60, 'puntuacion'] += 5
print(df)


#Ordena los estudiantes por puntuación de mayor a menor (sort_values).

