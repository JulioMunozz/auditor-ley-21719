from faker import Faker
import pandas as pd

Faker.seed(42)  # para que los datos sean reproducibles
fake = Faker('es_CL')

clientes = []
for i in range(100):
    cliente = {
        "nombre": fake.name(),
        "rut": fake.unique.rut(),
        "direccion": fake.address().replace("\n", ", "),
        "telefono": fake.phone_number(),
        "email": fake.email(),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
        "genero": fake.random_element(elements=("Masculino", "Femenino")),
        "estado_civil": fake.random_element(elements=("Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a")),
    }
    clientes.append(cliente)

df = pd.DataFrame(clientes)
df.to_csv("clientes.csv", index=False, encoding="utf-8-sig")

print(df.shape)   # debería salir (100, 8)
print(df.head())
