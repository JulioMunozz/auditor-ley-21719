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

-- 6) ¿Qué productos se venden más? Cantidad, monto total y promedio por producto
SELECT producto,
       COUNT(*) AS cantidad_ventas,
       SUM(monto) AS monto_total,
       ROUND(AVG(monto)) AS monto_promedio
FROM ventas
GROUP BY producto
ORDER BY monto_total DESC;

-- 7) ¿Cómo se reparten las ventas en el año? Cantidad y monto total por mes
SELECT strftime('%Y-%m', fecha) AS mes,
       COUNT(*) AS cantidad_ventas,
       SUM(monto) AS monto_total
FROM ventas
GROUP BY mes
ORDER BY mes;

-- 8) ¿Qué empleados venden más? Ranking por monto vendido
SELECT empleados.nombre,
       COUNT(ventas.id) AS cantidad_ventas,
       SUM(ventas.monto) AS monto_total
FROM ventas
INNER JOIN empleados ON ventas.empleado_id = empleados.id
GROUP BY empleados.id, empleados.nombre
ORDER BY monto_total DESC;

-- 9) ¿Quiénes son los 5 clientes que más gastan?
SELECT clientes.nombre,
       COUNT(ventas.id) AS cantidad_compras,
       SUM(ventas.monto) AS monto_total
FROM ventas
INNER JOIN clientes ON ventas.cliente_id = clientes.id
GROUP BY clientes.id, clientes.nombre
ORDER BY monto_total DESC
LIMIT 5;

-- 10) ¿Quiénes son los clientes frecuentes? Clientes con 5 compras o más
SELECT clientes.nombre,
       COUNT(ventas.id) AS cantidad_compras,
       SUM(ventas.monto) AS monto_total
FROM ventas
INNER JOIN clientes ON ventas.cliente_id = clientes.id
GROUP BY clientes.id, clientes.nombre
HAVING COUNT(ventas.id) >= 5
ORDER BY cantidad_compras DESC;