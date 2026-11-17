"""Audita cada columna de clientes.csv y empleados.csv combinando valores y nombre de columna."""

import pandas as pd

from auditor.columnas import auditar_columna

for archivo in ("clientes.csv", "empleados.csv"):
    df = pd.read_csv(archivo)
    print(f"\n===== {archivo} =====")
    print(f"{'Columna':<18} {'Tipo':<20} {'Categoría':<10} {'% valor':>8}  Detectado por")
    for columna in df.columns:
        h = auditar_columna(columna, df[columna])
        if h is None:
            print(f"{columna:<18} -")
        else:
            print(f"{columna:<18} {h['tipo']:<20} {h['categoria']:<10} {h['porcentaje']:>7}%  {h['detectado_por']}")