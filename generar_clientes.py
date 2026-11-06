import random
 
from faker import Faker
import pandas as pd
 
from rut import validar_rut
 
SEMILLA = 42
N_CLIENTES = 100
N_RUT_SUCIOS = 5  # RUT con DV incorrecto, para que el auditor tenga algo que detectar
 
Faker.seed(SEMILLA)  # fija la semilla de Faker
random.seed(SEMILLA)  # fija la semilla de random (la usamos para ensuciar RUT)
fake = Faker("es_CL")
 
 
def ensuciar_rut(rut):
    """Cambia el dígito verificador por uno incorrecto."""
    cuerpo, dv = rut[:-1], rut[-1]
    opciones = [d for d in "0123456789K" if d != dv]
    return cuerpo + random.choice(opciones)
 
 
indices_sucios = set(random.sample(range(N_CLIENTES), N_RUT_SUCIOS))
 
clientes = []
for i in range(N_CLIENTES):
    rut = fake.unique.rut()
    if i in indices_sucios:
        rut = ensuciar_rut(rut)
 
    cliente = {
        "nombre": fake.name(),
        "rut": rut,
        "direccion": fake.address().replace("\n", ", "),
        "telefono": fake.phone_number(),
        "email": fake.email(),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
        "genero": fake.random_element(elements=("Masculino", "Femenino")),
        "estado_civil": fake.random_element(elements=("Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a")),
        "ip": fake.ipv4_private(),
        "patente": fake.license_plate(),
        "cuenta_bancaria": fake.bban(),
        "sueldo": fake.random_int(min=500_000, max=3_000_000),
    }
    clientes.append(cliente)
 
df = pd.DataFrame(clientes)
df.to_csv("clientes.csv", index=False, encoding="utf-8-sig")
 
print(df.shape)  # debería salir (100, 12)
print(df.head())
 
# Chequeo rápido: ¿cuántos RUT inválidos quedaron?
validos = df["rut"].apply(validar_rut)
print(f"\nRUT inválidos: {(~validos).sum()} de {len(df)}")  # debería salir 5
 