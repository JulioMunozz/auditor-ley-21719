-- 1) ¿Qué compró cada cliente? Ventas con el nombre del cliente
SELECT ventas.id, ventas.fecha, ventas.producto, ventas.monto,
       clientes.nombre AS cliente
FROM ventas
INNER JOIN clientes ON ventas.cliente_id = clientes.id
ORDER BY ventas.fecha;

-- 2) ¿Qué empleado hizo cada venta? Ventas con el nombre del empleado
SELECT ventas.id, ventas.fecha, ventas.producto, ventas.monto,
       empleados.nombre AS empleado
FROM ventas
INNER JOIN empleados ON ventas.empleado_id = empleados.id
ORDER BY ventas.fecha;

-- 3) ¿Quién le vendió qué a quién? Ventas con cliente y empleado
SELECT ventas.id, ventas.fecha, ventas.producto, ventas.monto,
       clientes.nombre AS cliente,
       empleados.nombre AS empleado
FROM ventas
INNER JOIN clientes ON ventas.cliente_id = clientes.id
INNER JOIN empleados ON ventas.empleado_id = empleados.id
ORDER BY ventas.fecha;

-- 4) ¿Qué clientes nunca han comprado?
SELECT clientes.id, clientes.nombre, clientes.email
FROM clientes
LEFT JOIN ventas ON ventas.cliente_id = clientes.id
WHERE ventas.id IS NULL;

-- 5) ¿Qué empleados no han hecho ninguna venta?
SELECT empleados.id, empleados.nombre, empleados.cargo
FROM empleados
LEFT JOIN ventas ON ventas.empleado_id = empleados.id
WHERE ventas.id IS NULL;