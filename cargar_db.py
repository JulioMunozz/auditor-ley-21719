import sqlite3
import pandas as pd


conn = sqlite3.connect("pyme.db")            


df_clientes = pd.read_csv("clientes.csv")    
df_empleados = pd.read_csv("empleados.csv")
df_ventas = pd.read_csv("ventas.csv")           

df_clientes.to_sql("clientes", conn, if_exists="replace", index=False)
df_empleados.to_sql("empleados", conn, if_exists="replace", index=False)   
df_ventas.to_sql("ventas", conn, if_exists="replace", index=False)


print("Clientes:")
print(pd.read_sql("SELECT COUNT(*) FROM clientes", conn))

print("Empleados:")
print(pd.read_sql("SELECT COUNT(*) FROM empleados", conn))  

print("Ventas:")
print(pd.read_sql("SELECT COUNT(*) FROM ventas", conn))

print("Ventas huérfanas:")
print(pd.read_sql("""
    SELECT ventas.id_venta, ventas.rut_cliente
    FROM ventas
    LEFT JOIN clientes ON ventas.rut_cliente = clientes.rut
    WHERE clientes.rut IS NULL
""", conn))

conn.close()