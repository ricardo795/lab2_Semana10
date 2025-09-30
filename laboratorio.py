import pandas as pd
import numpy as np

# Cargar datos
datos = pd.read_csv('datos_canciones.csv')
print("Dataset completo:")
print(datos)

# 1. Mostrar primeros y últimos registros
print("\nPrimeros 5 registros:")
print(datos.head())
print("\nÚltimos 5 registros:")
print(datos.tail())

# 2. Resumen estadístico
print("\nResumen estadístico:")
describe = datos.describe()
print(describe)

# 3. Tipos de datos de cada columna
print("\nTipos de datos por columna:")
print(datos.dtypes)

# 4. Ordenar por una columna numérica (ejemplo: 'popularidad')
if 'popularidad' in datos.columns:
    print("\nCanciones ordenadas por popularidad (descendente):")
    print(datos.sort_values(by='popularidad', ascending=False).head())
else:
    print("\nNo se encontró la columna 'popularidad' para ordenar.")

# 5. Medidas estadísticas sobre una columna (ejemplo: 'duracion')
columna = 'duracion' if 'duracion' in datos.columns else datos.select_dtypes(include=np.number).columns[0]
print(f"\nMedidas estadísticas para la columna '{columna}':")
media = np.mean(datos[columna])
mediana = np.median(datos[columna])
desviacion = np.std(datos[columna])
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")





