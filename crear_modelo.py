"""Crea pyme_modelo.db desde schema.sql, carga clientes y empleados, y genera 300 ventas."""

import random
import sqlite3
from pathlib import Path

from faker import Faker
import pandas as pd

DB = "pyme_modelo.db"
SEMILLA = 42
N_VENTAS = 300
N_EMPLEADOS_SIN_VENTAS = 3  # empleados que no venden nada, para que la consulta 5 tenga filas
PRODUCTOS = ("Notebook", "Mouse", "Teclado", "Monitor", "Impresora", "Audífonos", "Disco SSD", "Webcam")

Faker.seed(SEMILLA)  # fija la semilla de Faker
random.seed(SEMILLA)  # fija la semilla de random
fake = Faker("es_CL")

# 1. Partir de cero: borrar la base si ya existe
Path(DB).unlink(missing_ok=True)

# 2. Conectarse y activar las claves foráneas
conn = sqlite3.connect(DB)
conn.execute("PRAGMA foreign_keys = ON")

# 3. Crear las tablas desde schema.sql
with open("schema.sql", encoding="utf-8") as archivo:
    conn.executescript(archivo.read())

# 4. Cargar clientes y empleados en las tablas que ya existen
df_clientes = pd.read_csv("clientes.csv")
df_empleados = pd.read_csv("empleados.csv")

df_clientes.to_sql("clientes", conn, if_exists="append", index=False)
df_empleados.to_sql("empleados", conn, if_exists="append", index=False)

# 5. Generar ventas usando solo IDs que existen de verdad
ids_clientes = [fila[0] for fila in conn.execute("SELECT id FROM clientes ORDER BY id").fetchall()]
ids_empleados = [fila[0] for fila in conn.execute("SELECT id FROM empleados ORDER BY id").fetchall()]
ids_vendedores = ids_empleados[:-N_EMPLEADOS_SIN_VENTAS]  # los últimos 3 empleados quedan sin ventas

ventas = []
for _ in range(N_VENTAS):
    venta = (
        random.choice(ids_clientes),  # cliente_id
        random.choice(ids_vendedores),  # empleado_id
        fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),  # fecha
        fake.random_element(elements=PRODUCTOS),  # producto
        fake.random_int(min=5_000, max=1_500_000),  # monto
    )
    ventas.append(venta)

conn.executemany(
    "INSERT INTO ventas (cliente_id, empleado_id, fecha, producto, monto) VALUES (?, ?, ?, ?, ?)",
    ventas,
)
conn.commit()  # obligatorio: guarda las ventas insertadas

# 6. Comprobar cuántas filas quedaron
for tabla in ("clientes", "empleados", "ventas"):
    total = conn.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
    print(f"{tabla.capitalize()}: {total}")

conn.close()