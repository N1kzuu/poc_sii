
import pandas as pd

# Cargar la base de datos principal
df = pd.read_csv("PUB_EMPRESAS_PJ_2020_A_2024.txt", sep="\t", encoding="utf-8")

# Normalizar nombres de columnas
df.columns = [col.strip().lower() for col in df.columns]

# Supongamos que las columnas relevantes son:
# - "region": Indica la región del registro
# - "caracterizado": Indica si el registro está caracterizado (1 = Sí, 0 = No)

# Verificar las primeras filas
print(df.head())

# Agrupar por región y contar caracterizados
resumen = df.groupby("Región")["caracterizado"].value_counts().unstack(fill_value=0)

# Renombrar columnas para mayor claridad
resumen.columns = ["no_caracterizados", "caracterizados"]

# Agregar un total por región
resumen["total"] = resumen["no_caracterizados"] + resumen["caracterizados"]

# Mostrar el resumen
print(resumen)

# Guardar el resumen en un archivo CSV o JSON
resumen.to_csv("resumen_por_region.csv", encoding="utf-8")
print("Resumen guardado en 'resumen_por_region.csv'")