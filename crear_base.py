import sqlite3

# Crear (o abrir) la base de datos
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()

# Borrar la tabla si ya existía, para no duplicar datos
cursor.execute("DROP TABLE IF EXISTS ventas")

# Crear la tabla de ventas
cursor.execute("""
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY,
    cliente TEXT,
    producto TEXT,
    monto REAL,
    fecha TEXT
)
""")

# Cargar datos de ejemplo
ventas = [
    ("Ana Perez", "Mouse", 1200.0, "2026-09-01"),
    ("Juan Gomez", "Teclado", 3500.5, "2026-09-01"),
    ("Luis Diaz", "Monitor", 45000.0, "2026-09-03"),
    ("Ana Perez", "Teclado", 3500.5, "2026-09-05"),
    ("Sofia Lopez", "Monitor", 45000.0, "2026-09-07"),
    ("Juan Gomez", "Mouse", 1200.0, "2026-09-08"),
]
cursor.executemany(
    "INSERT INTO ventas (cliente, producto, monto, fecha) VALUES (?, ?, ?, ?)",
    ventas,
)

conexion.commit()
conexion.close()
print("Base de datos creada con", len(ventas), "ventas")