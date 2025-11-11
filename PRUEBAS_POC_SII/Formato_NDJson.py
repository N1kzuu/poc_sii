import pandas as pd
import os  # Importar módulo para manejar directorios

source_path = "./PUB_EMPRESAS_PJ_2020_A_2024.txt"  # ajusta a tu ruta local
out_path    = "./empresas_pj_2020_2024.ndjson"  # Cambiar a una ruta válida en tu sistema
sep         = "\t"
encoding    = "utf-8"
chunksize   = 100_000

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

with pd.read_csv(source_path, sep=sep, encoding=encoding, chunksize=chunksize) as reader:
    first = True
    for chunk in reader:
        chunk.columns = normalize_cols(chunk.columns)
        mode = "w" if first else "a"
        chunk.to_json(out_path, orient="records", lines=True, force_ascii=False, mode=mode)
        first = False

print("Listo ->", out_path)