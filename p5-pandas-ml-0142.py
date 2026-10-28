
import numpy as np
import pandas as pd

## yahir sifuentes NC = 0142

## datos matriz 4 x 3
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# poner nombre a las columnas
# almacenar la tabla en la variable df
print("--- datos a partir de una matriz 4 x 3 ---")
df = pd.DataFrame(datos_alumno, columns=['ci', 'marcas', 'paquete'])
print(df)

# datos a partir de un diccionario
print("--- datos a partir de un diccionario 4 x 3 ---")
alumno_diccionario = {
    'nombre': ["Darrell", "Iris", "alex", "yeikop", "alexia", "farfan"],
    'califa': [90, 70, 100, 80, 60, 70],
    'edad': [16, 17, 16, 16, 17, 16]
}

# convertir el diccionario en un DataFrame
df_alumnos = pd.DataFrame(alumno_diccionario)
print(df_alumnos)

print("yahir sifuentes NC = 0142")



