import sqlite3
import pandas as pd

# 1. Conectarte a la nueva base
conn = sqlite3.connect("pyme.db")            # ← cambió el nombre

# 2. Leer los dos CSV
df_clientes = pd.read_csv("clientes.csv")    # ← antes se llamaba df
df_empleados = pd.read_csv("empleados.csv")            # ← completa: el otro CSV

# 3. Guardar cada DataFrame como tabla
df_clientes.to_sql("clientes", conn, if_exists="replace", index=False)
df_empleados.to_sql("empleados", conn, if_exists="replace", index=False)   # ← completa: nombre de la tabla

# 4. Contar filas en cada tabla
print("Clientes:")
print(pd.read_sql("SELECT COUNT(*) FROM clientes", conn))

print("Empleados:")
print(pd.read_sql("SELECT COUNT(*) FROM empleados", conn))   # ← completa: la misma tabla del paso 3

conn.close()