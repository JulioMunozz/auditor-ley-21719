# auditor-ley-21719

Auditor de datos personales según la Ley 21.719 (Chile), con datos ficticios.

Proyecto personal que detecta datos personales en las bases de una pyme ficticia, mide su calidad y duplicados, los clasifica con IA y muestra los resultados en un dashboard.

> Aviso: todos los datos de este repositorio son ficticios, generados con Faker. No hay datos reales de personas.

## Tecnologías

- Python (pandas, Faker)
- SQL
- Power BI

## Estructura del repositorio

| Archivo | Descripción |
|---|---|
| generar_clientes.py | Script que genera clientes ficticios con Faker |
| clientes.csv | Archivo de salida con los datos generados |
| requirements.txt | Dependencias de Python |
| README.md | Este archivo |

## Cómo ejecutar el generador de datos

1. Clona el repositorio:
   

git clone https://github.com/JulioMunozz/auditor-ley-21719.git
cd auditor-ley-21719
2. (Opcional) Crea un entorno virtual:
   

python -m venv venv
venv\Scripts\activate
   En Mac/Linux se activa con source venv/bin/activate.
3. Instala las dependencias:
   

pip install -r requirements.txt
4. Ejecuta el script desde la carpeta raíz del repositorio:
   

python generar_clientes.py
5. Se crea (o se sobrescribe) el archivo clientes.csv con datos ficticios.

Detalles del archivo generado:
- Cantidad de clientes: 100
- Columnas (12): nombre, rut, direccion, telefono, email, fecha_nacimiento, genero, estado_civil, ip, patente, cuenta_bancaria, sueldo
- Los datos son reproducibles: el script usa una semilla fija, así que cada ejecución genera el mismo CSV.

## Catálogo de datos que detecta el auditor

Las tablas siguientes son el catálogo de datos que el auditor debe detectar. Los datos personales de la primera tabla están en clientes.csv; los datos sensibles son un catálogo de referencia y todavía no están en el CSV.

### Datos personales (12 ejemplos)

| Dato | Tipo | Cómo se vería (ficticio) | En el CSV |
|---|---|---|---|
| Nombre completo | Personal | Ana Pérez Soto | Sí |
| RUT | Personal | 12.345.678-5 | Sí |
| Correo electrónico | Personal | ana.perez@example.com | Sí |
| Teléfono | Personal | +56 9 1234 5678 | Sí |
| Dirección | Personal | Calle Falsa 123, Maipú | Sí |
| Fecha de nacimiento | Personal | 1990-05-14 | Sí |
| Género | Personal | Femenino | Sí |
| Estado civil | Personal | Soltero/a | Sí |
| Dirección IP | Personal | 192.168.1.45 | Sí |
| Patente de vehículo | Personal | ABCD-12 | Sí |
| Número de cuenta bancaria | Personal | 000123456789 | Sí |
| Sueldo | Personal | $1.200.000 | Sí |

### Datos sensibles (5 ejemplos)

| Dato | Tipo | Cómo se vería (ficticio) | En el CSV |
|---|---|---|---|
| Diagnóstico médico | Sensible | "Diabetes tipo 2" | No |
| Afiliación sindical | Sensible | "Socio Sindicato Ejemplo" | No |
| Origen étnico | Sensible | "Pueblo mapuche" | No |
| Creencia religiosa | Sensible | "Católico" | No |
| Dato biométrico | Sensible | Huella dactilar (hash ficticio: a3f9c1...) | No |

## Avance del proyecto

- [x] Generación de datos ficticios con Faker
- [ ] Consultas SQL de calidad y duplicados
- [ ] Clasificación con IA
- [ ] Dashboard en Power BI