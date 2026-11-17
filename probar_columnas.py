"""Analiza cada columna de clientes.csv y muestra qué tipo de dato personal contiene."""

import pandas as pd

from auditor.columnas import UMBRAL, analizar_columna

df = pd.read_csv("clientes.csv")

print(f"{'Columna':<18} {'Tipo':<10} {'% calza':>8}  Marcada (>= {UMBRAL}%)")
for columna in df.columns:
    r = analizar_columna(df[columna])
    tipo = r["tipo"] or "-"
    marcada = "Sí" if r["marcada"] else "No"
    print(f"{columna:<18} {tipo:<10} {r['porcentaje']:>7}%  {marcada}")