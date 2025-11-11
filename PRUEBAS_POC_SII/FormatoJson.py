import pandas as pd
import os  # Importar módulo para manejar directorios

source_path = "./PUB_EMPRESAS_PJ_2020_A_2024.txt"  # ajusta a tu ruta local
out_path    = "./empresas_pj_2020_2024.json"  # Cambiar a una ruta válida en tu sistema
sep         = "\t"
encoding    = "utf-8"

# Crear el directorio de salida si no existe
output_dir = os.path.dirname(out_path)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Normalización de nombres
import re
def normalize_cols(cols):
    ncols = []
    for c in cols:
        nc = re.sub(r"[^0-9a-zA-Z_]", "_", str(c).strip())
        nc = re.sub(r"_+", "_", nc).strip("_").lower()
        ncols.append(nc)
    return ncols

# Leer el archivo completo y convertir a JSON
df = pd.read_csv(source_path, sep=sep, encoding=encoding)
df.columns = normalize_cols(df.columns)

# Guardar como un único archivo JSON
df.to_json(out_path, orient="records", force_ascii=False, indent=4)

print("Listo ->", out_path)