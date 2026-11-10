-- Modelo de datos de la pyme ficticia (Auditor Ley 21.719)
-- Cada venta pertenece a un cliente y fue hecha por un empleado.

PRAGMA foreign_keys = ON;

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rut TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    email TEXT,
    fecha_nacimiento DATE,
    genero TEXT,
    estado_civil TEXT,
    ip TEXT,
    patente TEXT,
    cuenta_bancaria TEXT,
    sueldo INTEGER
);

CREATE TABLE empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rut TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL,
    cargo TEXT,
    fecha_ingreso DATE,
    sueldo INTEGER,
    correo TEXT UNIQUE
);

CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    empleado_id INTEGER NOT NULL,
    fecha DATE NOT NULL,
    producto TEXT NOT NULL,
    monto INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);