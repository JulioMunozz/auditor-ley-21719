import sqlite3

conn = sqlite3.connect(":memory:")  # base temporal, no crea archivos

with open("schema.sql", encoding="utf-8") as archivo:
    conn.executescript(archivo.read())

tablas = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tablas creadas:", [t[0] for t in tablas])

conn.execute("INSERT INTO clientes (rut, nombre) VALUES ('12.345.678-5', 'Cliente de prueba')")
conn.execute("INSERT INTO empleados (rut, nombre) VALUES ('11.111.112-K', 'Empleado de prueba')")
conn.execute("INSERT INTO ventas (cliente_id, empleado_id, fecha, producto, monto) VALUES (1, 1, '2026-01-15', 'Mouse', 15000)")
print("Venta válida: insertada")

try:
    conn.execute("INSERT INTO ventas (cliente_id, empleado_id, fecha, producto, monto) VALUES (99, 1, '2026-01-15', 'Mouse', 15000)")
    print("Venta huérfana: insertada (las FK NO están funcionando)")
except sqlite3.IntegrityError as error:
    print("Venta huérfana: bloqueada ->", error)

conn.close()