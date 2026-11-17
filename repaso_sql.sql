-- 1) Empleados con su cantidad de ventas, incluyendo los que tienen 0
SELECT empleados.nombre, COUNT(ventas.id) AS cantidad_ventas
FROM empleados
LEFT JOIN ventas ON ventas.empleado_id = empleados.id
GROUP BY empleados.id, empleados.nombre
ORDER BY cantidad_ventas;

-- 2) Monto total por mes, solo de los meses que superan el promedio mensual
SELECT strftime('%Y-%m', fecha) AS mes,
       SUM(monto) AS monto_total
FROM ventas
GROUP BY mes
HAVING SUM(monto) > (
    SELECT AVG(total)
    FROM (
        SELECT SUM(monto) AS total
        FROM ventas
        GROUP BY strftime('%Y-%m', fecha)
    )
)
ORDER BY mes;


-- 3) Clientes que nunca han comprado (LEFT JOIN + IS NULL)
SELECT clientes.id, clientes.nombre, clientes.email
FROM clientes
LEFT JOIN ventas ON ventas.cliente_id = clientes.id
WHERE ventas.cliente_id IS NULL;