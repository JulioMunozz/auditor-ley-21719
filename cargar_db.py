import sqlite3
import pandas as pd

# 1. Conectarte a la nueva base
conn = sqlite3.connect("pyme.db")            

# 2. Leer los dos CSV
df_clientes = pd.read_csv("clientes.csv")    
df_empleados = pd.read_csv("empleados.csv")            

# 3. Guardar cada DataFrame como tabla
df_clientes.to_sql("clientes", conn, if_exists="replace", index=False)
df_empleados.to_sql("empleados", conn, if_exists="replace", index=False)   

# 4. Contar filas en cada tabla
print("Clientes:")
print(pd.read_sql("SELECT COUNT(*) FROM clientes", conn))

print("Empleados:")
print(pd.read_sql("SELECT COUNT(*) FROM empleados", conn))  

conn.close()