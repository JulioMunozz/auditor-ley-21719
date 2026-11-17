"""Ejecuta cada consulta de consultas.sql contra pyme.db y muestra el resultado."""

import sqlite3

import pandas as pd

import sys
archivo_sql = sys.argv[1] if len(sys.argv) > 1 else "consultas.sql"
with open(archivo_sql, encoding="utf-8") as archivo:
    texto = archivo.read()

# Cada consulta termina en ";", así que separamos por ese carácter
consultas = [c.strip() for c in texto.split(";") if c.strip()]

conn = sqlite3.connect("pyme_modelo.db")
for numero, consulta in enumerate(consultas, start=1):
    print(f"\n===== Consulta {numero} =====")
    print(pd.read_sql(consulta, conn))
conn.close()