
import pandas as pd

# Cargar la base de datos principal
df = pd.read_csv("PUB_EMPRESAS_PJ_2020_A_2024.txt", sep="\t", encoding="utf-8")

# Mostrar los nombres de las columnas disponibles en el archivo
print("Columnas disponibles en el archivo:")
print(df.columns)

# Mostrar las primeras filas del DataFrame para verificar el contenido
print("\nPrimeras filas del archivo:")
print(df.head())