"""Auditor de datos personales: recorre una base SQLite y detecta RUT, correos y teléfonos."""

import argparse
import sqlite3
from collections import Counter
from datetime import datetime

from auditor.patrones import detectar_columna, detectar_valor, enmascarar

# 1. Leer el argumento --fuente desde la terminal
parser = argparse.ArgumentParser(description="Detecta datos personales en una base SQLite.")
parser.add_argument("--fuente", required=True, help="Ruta de la base SQLite a auditar")
args = parser.parse_args()

conn = sqlite3.connect(args.fuente)

# 2. Listar las tablas de la base (sin las internas de SQLite ni la de hallazgos)
tablas = [
    fila[0]
    for fila in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' "
        "AND name != 'hallazgos' ORDER BY name"
    )
]

# 3. Recorrer cada columna de cada tabla
hallazgos = []
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for tabla in tablas:
    columnas = [fila[1] for fila in conn.execute(f"PRAGMA table_info({tabla})")]
    for columna in columnas:
        valores = [fila[0] for fila in conn.execute(f"SELECT {columna} FROM {tabla}")]

        # Detección por valores: cuántos valores calzan con cada tipo
        conteo = Counter(detectar_valor(v) for v in valores)
        conteo.pop(None, None)  # descartar los que no calzaron con nada

        # Detección por nombre de la columna
        tipo_nombre = detectar_columna(columna)

        if conteo or tipo_nombre:
            tipo_valor, cantidad = conteo.most_common(1)[0] if conteo else (None, 0)
            tipo = tipo_valor or tipo_nombre
            if tipo_valor and tipo_nombre:
                metodo = "valor y nombre"
            elif tipo_valor:
                metodo = "solo valor"
            else:
                metodo = "solo nombre"

            ejemplo_real = next((v for v in valores if v), "")
            hallazgos.append((fecha, tabla, columna, tipo, metodo, cantidad, len(valores), enmascarar(ejemplo_real, tipo)))

# 4. Guardar los hallazgos en una tabla de la misma base
conn.execute("DROP TABLE IF EXISTS hallazgos")
conn.execute("""
    CREATE TABLE hallazgos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_auditoria TEXT,
        tabla TEXT,
        columna TEXT,
        tipo TEXT,
        metodo TEXT,
        coincidencias INTEGER,
        total_filas INTEGER,
        ejemplo TEXT
    )
""")
conn.executemany(
    "INSERT INTO hallazgos (fecha_auditoria, tabla, columna, tipo, metodo, coincidencias, total_filas, ejemplo) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    hallazgos,
)
conn.commit()

# 5. Mostrar el resumen en la terminal
print(f"\nAuditoría de {args.fuente} ({fecha})")
print(f"Tablas revisadas: {len(tablas)} | Columnas con datos personales: {len(hallazgos)}\n")
print(f"{'Tabla.columna':<20} {'Tipo':<10} {'Método':<16} {'Coincidencias':<14} Ejemplo")
for _, tabla, columna, tipo, metodo, cantidad, total, ejemplo in hallazgos:
    print(f"{tabla + '.' + columna:<20} {tipo:<10} {metodo:<16} {f'{cantidad}/{total}':<14} {ejemplo}")

print("\nColumnas por tipo:")
for tipo, cantidad in Counter(h[3] for h in hallazgos).items():
    print(f"  {tipo}: {cantidad}")
print("\nHallazgos guardados en la tabla 'hallazgos'.")

conn.close()