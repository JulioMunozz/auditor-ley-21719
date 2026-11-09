import sqlite3
import pandas as pd

# 1. Conectarte (si el archivo no existe, se crea)
conn = sqlite3.connect("auditor.db")

# 2. Leer el CSV con pandas
df = pd.read_csv("clientes.csv")

# 3. Guardar el DataFrame como tabla "clientes"
df.to_sql("clientes", conn, if_exists="replace", index=False)

# 4. Tu primera consulta SQL
resultado = pd.read_sql("SELECT COUNT(*) FROM clientes", conn)
print(resultado)

conn.close()