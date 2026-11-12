-- Resumen de ventas por cliente: cuántas compras hizo y cuánto gastó en total
SELECT clientes.nombre,
       COUNT(ventas.id_venta) AS cantidad_ventas,
       SUM(ventas.monto) AS monto_total
FROM clientes
INNER JOIN ventas ON clientes.rut = ventas.rut_cliente
GROUP BY clientes.rut, clientes.nombre
ORDER BY monto_total DESC;


--VENTAS HUERFANAS: ventas que no tienen un cliente asociado
 SELECT ventas.id_venta, ventas.rut_cliente
    FROM ventas
    LEFT JOIN clientes ON ventas.rut_cliente = clientes.rut
    WHERE clientes.rut IS NULL;