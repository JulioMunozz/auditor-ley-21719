# auditor-ley-21719

Auditor de datos personales según la Ley 21.719 (Chile), con datos ficticios.

Proyecto personal que detecta datos personales en las bases de una pyme ficticia, mide su calidad y duplicados, los clasifica con IA y muestra los resultados en un dashboard.

> Aviso: todos los datos de este repositorio son ficticios, generados con Faker. No hay datos reales de personas.

## Tecnologías

- Python (pandas, Faker, pytest)
- SQL (SQLite)
- Power BI

## Estructura del repositorio

| Archivo | Descripción |
|---|---|
| rut.py | Funciones para calcular, validar y generar RUT con el algoritmo módulo 11 |
| test_rut.py | Pruebas automáticas de `validar_rut` con pytest |
| generar_clientes.py | Genera 100 clientes ficticios (con 5 RUT inválidos a propósito) |
| generar_empleados.py | Genera 50 empleados ficticios con RUT válido y correo corporativo |
| generar_ventas.py | Genera 300 ventas ligadas a clientes (con 3 ventas huérfanas a propósito) |
| cargar_db.py | Carga los tres CSV como tablas en la base SQLite `pyme.db` |
| consultas.sql | Consultas SQL del auditor (resumen por cliente y ventas huérfanas) |
| ejecutar_consultas.py | Ejecuta las consultas de `consultas.sql` contra `pyme.db` |
| schema.sql | Modelo de datos con CREATE TABLE, claves primarias y foráneas |
| probar_schema.py | Prueba que schema.sql crea las tablas y que las FK bloquean ventas huérfanas |
| diagrama.png | Diagrama del modelo de datos |
| clientes.csv, empleados.csv, ventas.csv | Datos ficticios generados por los scripts |
| requirements.txt | Dependencias de Python |

## Modelo de datos

![Diagrama del modelo](diagrama.png)

Cada venta pertenece a un cliente (`ventas.cliente_id`) y fue hecha por un empleado (`ventas.empleado_id`). El modelo completo está en `schema.sql`.

> Este es el diseño objetivo. Por ahora los scripts generan las ventas ligadas a clientes por `rut_cliente`; adaptarlos al modelo es un paso siguiente.

Para comprobar que el modelo funciona:

```
python probar_schema.py
```

## Cómo usarlo

1. Clona el repositorio:

   ```
   git clone https://github.com/JulioMunozz/auditor-ley-21719.git
   cd auditor-ley-21719
   ```

2. (Opcional) Crea y activa un entorno virtual:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   En Mac/Linux se activa con `source venv/bin/activate`.

3. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

4. Genera los datos ficticios. El orden importa: `generar_ventas.py` usa los RUT de `clientes.csv`, así que los clientes van primero.

   ```
   python generar_clientes.py
   python generar_empleados.py
   python generar_ventas.py
   ```

5. Crea la base de datos `pyme.db` con las tablas `clientes`, `empleados` y `ventas`:

   ```
   python cargar_db.py
   ```

   Al final muestra los conteos de cada tabla (100, 50 y 300) y las ventas huérfanas.

6. Ejecuta las consultas del auditor:

   ```
   python ejecutar_consultas.py
   ```

7. (Opcional) Corre las pruebas automáticas:

   ```
   python -m pytest -v
   ```

> `pyme.db` no se sube al repositorio (está en `.gitignore`) porque se puede regenerar en cualquier momento con los pasos 4 y 5.

### Detalles de los datos generados

- **clientes**: 100 filas, 12 columnas (nombre, rut, direccion, telefono, email, fecha_nacimiento, genero, estado_civil, ip, patente, cuenta_bancaria, sueldo).
- **empleados**: 50 filas, 6 columnas (nombre, rut, cargo, fecha_ingreso, sueldo, correo).
- **ventas**: 300 filas, 5 columnas (id_venta, rut_cliente, fecha, producto, monto).
- Los datos son reproducibles: todos los scripts usan la semilla 42, así que cada ejecución genera los mismos datos.
- Errores plantados a propósito para que el auditor los detecte: 5 clientes con RUT inválido y 3 ventas con un RUT que no existe en clientes (registros huérfanos).

## Catálogo de datos que detecta el auditor

Las tablas siguientes son el catálogo de datos que el auditor debe detectar. Los datos personales de la primera tabla están en los CSV generados; los datos sensibles son un catálogo de referencia y todavía no están en los datos.

### Datos personales (12 ejemplos)

| Dato | Tipo | Cómo se vería (ficticio) | Dónde está |
|---|---|---|---|
| Nombre completo | Personal | Ana Pérez Soto | clientes, empleados |
| RUT | Personal | 12.345.678-5 | clientes, empleados, ventas |
| Correo electrónico | Personal | ana.perez@example.com | clientes, empleados |
| Teléfono | Personal | +56 9 1234 5678 | clientes |
| Dirección | Personal | Calle Falsa 123, Maipú | clientes |
| Fecha de nacimiento | Personal | 1990-05-14 | clientes |
| Género | Personal | Femenino | clientes |
| Estado civil | Personal | Soltero/a | clientes |
| Dirección IP | Personal | 192.168.1.45 | clientes |
| Patente de vehículo | Personal | ABCD-12 | clientes |
| Número de cuenta bancaria | Personal | 000123456789 | clientes |
| Sueldo | Personal | $1.200.000 | clientes, empleados |

### Datos sensibles (5 ejemplos)

| Dato | Tipo | Cómo se vería (ficticio) | Dónde está |
|---|---|---|---|
| Diagnóstico médico | Sensible | "Diabetes tipo 2" | Todavía no |
| Afiliación sindical | Sensible | "Socio Sindicato Ejemplo" | Todavía no |
| Origen étnico | Sensible | "Pueblo mapuche" | Todavía no |
| Creencia religiosa | Sensible | "Católico" | Todavía no |
| Dato biométrico | Sensible | Huella dactilar (hash ficticio: a3f9c1...) | Todavía no |

## Avance del proyecto

- [x] Generación de datos ficticios con Faker (clientes, empleados y ventas)
- [x] Validación de RUT con módulo 11 y pruebas automáticas con pytest
- [x] Base de datos SQLite con las tres tablas
- [x] Primeras consultas SQL (resumen por cliente y detección de ventas huérfanas)
- [x] Modelo de datos (diagrama y schema.sql)
- [ ] Consultas SQL de calidad y duplicados
- [ ] Clasificación con IA
- [ ] Dashboard en Power BI