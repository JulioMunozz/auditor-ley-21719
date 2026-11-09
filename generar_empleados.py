import unicodedata

from faker import Faker
import pandas as pd

from rut import validar_rut

SEMILLA = 42
N_EMPLEADOS = 50
DOMINIO = "pymeficticia.cl"

Faker.seed(SEMILLA)  # para que los datos sean reproducibles
fake = Faker("es_CL")


def quitar_tildes(texto):
    """Convierte 'Víctor Muñoz' en 'Victor Munoz'."""
    normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normalizado if not unicodedata.combining(c))


def crear_correo(nombre):
    """Arma un correo corporativo: primernombre.primerapellido@dominio."""
    partes = quitar_tildes(nombre).lower().split()
    primer_nombre = partes[0]
    if len(partes) == 2:  # "Renato Martínez": nombre + un solo apellido
        primer_apellido = partes[1]
    else:  # el penúltimo, porque el último es el segundo apellido
        primer_apellido = partes[-2]
    return f"{primer_nombre}.{primer_apellido}@{DOMINIO}"


empleados = []
for _ in range(N_EMPLEADOS):
    nombre = fake.name()
    empleado = {
        "nombre": nombre,
        "rut": fake.unique.rut(),
        "cargo": fake.job(),
        "fecha_ingreso": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d"),
        "sueldo": fake.random_int(min=500_000, max=3_000_000),
        "correo": crear_correo(nombre),
    }
    empleados.append(empleado)

df = pd.DataFrame(empleados)
df.to_csv("empleados.csv", index=False, encoding="utf-8-sig")

print(df.shape)  # debería salir (50, 6)
print(df[["nombre", "correo"]].head())

# Chequeo: ¿todos los RUT son válidos?
validos = df["rut"].apply(validar_rut)
print(f"\nRUT inválidos: {(~validos).sum()} de {len(df)}")  # debería salir 0