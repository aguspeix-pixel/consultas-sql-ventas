import sqlite3

conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()

def consulta(titulo, sql):
    print("=" * 50)
    print(titulo)
    print("=" * 50)
    cursor.execute(sql)
    columnas = [c[0] for c in cursor.description]
    print(" | ".join(columnas))
    for fila in cursor.fetchall():
        print(" | ".join(str(x) for x in fila))
    print()

consulta("1. Total vendido",
         "SELECT SUM(monto) AS total FROM ventas")

consulta("2. Promedio por venta",
         "SELECT ROUND(AVG(monto), 2) AS promedio FROM ventas")

consulta("3. Total por cliente (de mayor a menor)",
         "SELECT cliente, SUM(monto) AS total FROM ventas "
         "GROUP BY cliente ORDER BY total DESC")

consulta("4. Ranking de productos",
         "SELECT producto, COUNT(*) AS cantidad, SUM(monto) AS total "
         "FROM ventas GROUP BY producto ORDER BY total DESC")

consulta("5. Ventas mayores a 10.000",
         "SELECT cliente, producto, monto FROM ventas "
         "WHERE monto > 10000 ORDER BY monto DESC")

conexion.close()