import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# =========================
# CONFIGURACIÓN DE CONEXIÓN
# =========================
HOST = "localhost"
USER = "root"
PASSWORD = "ROOT"  # pon tu contraseña de MySQL aquí


def conectar_mysql():
    """Conecta a MySQL y crea la BD si no existe"""
    try:
        conexion = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )
        cursor = conexion.cursor()
        print("Conexión exitosa a MySQL.")
        return conexion, cursor
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        exit()


# =========================
# CREAR BASE Y TABLAS
# =========================
def crear_base_datos(cursor, conexion):
    cursor.execute("DROP DATABASE IF EXISTS tienda_db")
    cursor.execute("CREATE DATABASE tienda_db")
    cursor.execute("USE tienda_db")

    cursor.execute("""
    CREATE TABLE categorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        precio DECIMAL(10,2) NOT NULL,
        cantidad INT NOT NULL,
        categoria_id INT,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE ventas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        producto_id INT,
        fecha DATE,
        cantidad_vendida INT,
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    """)

    cursor.executemany("INSERT INTO categorias (nombre) VALUES (%s)", [
        ("Electrónicos",), ("Ropa",), ("Alimentos",), ("Hogar",)
    ])

    cursor.executemany("INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES (%s,%s,%s,%s)", [
        ("Laptop", 1200, 10, 1),
        ("Camisa", 25, 50, 2),
        ("Manzanas", 2, 200, 3),
        ("Silla", 75, 30, 4),
        ("Teléfono", 800, 15, 1)
    ])

    cursor.executemany("INSERT INTO ventas (producto_id, fecha, cantidad_vendida) VALUES (%s,%s,%s)", [
        (1, "2025-09-01", 2),
        (2, "2025-09-02", 5),
        (3, "2025-09-02", 20),
        (4, "2025-09-03", 3),
        (5, "2025-09-04", 1)
    ])

    conexion.commit()
    print("Base de datos y datos creados correctamente.")


# =========================
# FUNCIONES EXTRA
# =========================
def agregar_producto(cursor, conexion):
    print("\n--- Agregar un nuevo producto ---")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    categoria_id = int(input("ID de la categoría (1-Electrónicos, 2-Ropa, 3-Alimentos, 4-Hogar): "))

    cursor.execute(
        "INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES (%s,%s,%s,%s)",
        (nombre, precio, cantidad, categoria_id)
    )
    conexion.commit()
    print(f"Producto '{nombre}' agregado con éxito.")


def buscar_producto(cursor):
    print("\n--- Buscar producto ---")
    nombre = input("Nombre del producto a buscar: ")
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE %s", ("%" + nombre + "%",))
    resultados = cursor.fetchall()

    if resultados:
        for r in resultados:
            print(r)
    else:
        print("No se encontró el producto.")


def listar_productos(cursor):
    print("\n--- Lista de productos ---")
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    for r in resultados:
        print(r)


# =========================
# CLASES DE REPORTES
# =========================
class Estadistica:
    def __init__(self, ventas):
        self.ventas = ventas

    def mostrar(self):
        cantidades = [v[3] for v in self.ventas]
        print(f"\nTotal vendido: {sum(cantidades)}")
        print(f"Promedio por venta: {np.mean(cantidades):.2f}")
        print(f"Máximo vendido: {np.max(cantidades)}")
        print(f"Mínimo vendido: {np.min(cantidades)}")


class GraficaBar:
    def __init__(self, ventas):
        self.ventas = ventas

    def mostrar(self):
        productos = [v[1] for v in self.ventas]
        cantidades = [v[3] for v in self.ventas]
        plt.bar(productos, cantidades)
        plt.title("Ventas por producto")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad vendida")
        plt.show()


class GraficaScatter:
    def __init__(self, cursor):
        self.cursor = cursor

    def mostrar(self):
        self.cursor.execute("SELECT precio, cantidad FROM productos")
        datos = self.cursor.fetchall()
        precios, cantidades = zip(*datos)
        plt.scatter(precios, cantidades)
        plt.title("Precio vs Cantidad en stock")
        plt.xlabel("Precio")
        plt.ylabel("Cantidad en stock")
        plt.show()


class GraficaPie:
    def __init__(self, cursor):
        self.cursor = cursor

    def mostrar(self):
        self.cursor.execute("""
        SELECT c.nombre, SUM(p.cantidad)
        FROM productos p
        JOIN categorias c ON p.categoria_id = c.id
        GROUP BY c.nombre
        """)
        datos = self.cursor.fetchall()
        categorias, cantidades = zip(*datos)
        plt.pie(cantidades, labels=categorias, autopct="%1.1f%%")
        plt.title("Productos por categoría")
        plt.show()


# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
    conexion, cursor = conectar_mysql()
    crear_base_datos(cursor, conexion)

    # Usar la base ya creada
    cursor.execute("USE tienda_db")

    while True:
        # Consultar ventas actualizadas
        cursor.execute("""
        SELECT ventas.id, productos.nombre, ventas.fecha, ventas.cantidad_vendida
        FROM ventas
        JOIN productos ON ventas.producto_id = productos.id
        """)
        ventas = cursor.fetchall()

        print("\n====== MENÚ DE OPCIONES ======")
        print("1. Ver estadísticas básicas")
        print("2. Ver gráfica de ventas (bar)")
        print("3. Ver gráfica precio vs cantidad (scatter)")
        print("4. Ver gráfica por categoría (pie)")
        print("5. Agregar un producto")
        print("6. Buscar un producto")
        print("7. Listar productos")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            Estadistica(ventas).mostrar()
        elif opcion == "2":
            GraficaBar(ventas).mostrar()
        elif opcion == "3":
            GraficaScatter(cursor).mostrar()
        elif opcion == "4":
            GraficaPie(cursor).mostrar()
        elif opcion == "5":
            agregar_producto(cursor, conexion)
        elif opcion == "6":
            buscar_producto(cursor)
        elif opcion == "7":
            listar_productos(cursor)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

    cursor.close()
    conexion.close()
    print("Conexión cerrada correctamente.")
