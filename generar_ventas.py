import random

from faker import Faker
import pandas as pd

from rut import generar_rut

SEMILLA = 42
N_VENTAS = 300
N_HUERFANAS = 3  # ventas con un RUT que no existe en clientes, para que el auditor las detecte
PRODUCTOS = ("Notebook", "Mouse", "Teclado", "Monitor", "Impresora", "Audífonos", "Disco SSD", "Webcam")

Faker.seed(SEMILLA)  # fija la semilla de Faker
random.seed(SEMILLA)  # fija la semilla de random
fake = Faker("es_CL")

# Leer los RUT de los clientes
clientes = pd.read_csv("clientes.csv")
ruts = clientes["rut"].tolist()


def rut_inexistente():
    """Genera un RUT que no pertenece a ningún cliente."""
    rut = generar_rut()
    while rut in ruts:
        rut = generar_rut()
    return rut


indices_huerfanos = set(random.sample(range(N_VENTAS), N_HUERFANAS))

ventas = []
for i in range(N_VENTAS):
    rut_cliente = random.choice(ruts)
    if i in indices_huerfanos:
        rut_cliente = rut_inexistente()

    venta = {
        "id_venta": i + 1,
        "rut_cliente": rut_cliente,
        "fecha": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "producto": fake.random_element(elements=PRODUCTOS),
        "monto": fake.random_int(min=5_000, max=1_500_000),
    }
    ventas.append(venta)

df = pd.DataFrame(ventas)
df.to_csv("ventas.csv", index=False, encoding="utf-8-sig")

print(df.shape)  # debería salir (300, 5)
print(df.head())

# Chequeo: ¿cuántas ventas tienen un RUT que no está en clientes?
huerfanas = ~df["rut_cliente"].isin(ruts)
print(f"\nVentas huérfanas: {huerfanas.sum()}")  # debería salir 3
print(df[huerfanas])