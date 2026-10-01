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