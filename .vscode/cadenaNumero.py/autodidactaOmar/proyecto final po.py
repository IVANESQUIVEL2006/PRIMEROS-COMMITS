import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

HOST = "localhost"
USER = "root"
PASSWORD = "ROOT"

# -----------------------------
# Función para crear la conexión
# -----------------------------
def conectar_mysql():
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

# -----------------------------
# Función para crear base de datos y tablas
# -----------------------------
def crear_base_datos(cursor, conexion):
    cursor.execute("DROP DATABASE IF EXISTS tienda_db")
    cursor.execute("CREATE DATABASE tienda_db")
    cursor.execute("USE tienda_db")

    # Crear tablas
    cursor.execute("""
    CREATE TABLE categorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE proveedores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        telefono VARCHAR(20)
    )""")

    cursor.execute("""
    CREATE TABLE productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        precio DECIMAL(10,2) NOT NULL,
        cantidad INT NOT NULL,
        categoria_id INT,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )""")

    cursor.execute("""
    CREATE TABLE ventas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        producto_id INT NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        cantidad_vendida INT NOT NULL,
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )""")

    # Insertar datos
    cursor.executemany("INSERT INTO categorias (nombre) VALUES (%s)", [
        ('Electrónicos',),
        ('Ropa',),
        ('Alimentos',),
        ('Hogar',),
        ('Juguetes',)
    ])

    cursor.executemany("INSERT INTO proveedores (nombre, telefono) VALUES (%s, %s)", [
        ('TecnoSuministros', '555-100-2000'),
        ('ModaTotal', '555-100-3000'),
        ('AlimentosSA', '555-100-4000')
    ])

    cursor.executemany("""
    INSERT INTO productos (nombre, precio, cantidad, categoria_id) 
    VALUES (%s, %s, %s, %s)
    """, [
        ('Laptop', 1200.00, 15, 1),
        ('Smartphone', 800.00, 30, 1),
        ('Camisa', 25.50, 50, 2),
        ('Arroz', 3.20, 100, 3),
        ('Sofá', 450.00, 5, 4),
        ('Muñeca', 15.75, 20, 5)
    ])

    cursor.executemany("""
    INSERT INTO ventas (producto_id, cantidad_vendida)
    VALUES (%s, %s)
    """, [
        (1, 2), (2, 5), (3, 10), (4, 15), (5, 1), (6, 3), (2, 4), (3, 8), (4, 20)
    ])

    conexion.commit()
    print("Base de datos y datos creados correctamente.")

# -----------------------------
# Clases de Reportes
# -----------------------------
class Reporte(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Estadistica(Reporte):
    def __init__(self, datos):
        self.datos = datos

    def mostrar(self):
        cantidades = [v[3] for v in self.datos]
        print("Estadísticas:")
        print(f"Total vendido: {sum(cantidades)}")
        print(f"Promedio por venta: {np.mean(cantidades):.2f}")
        print(f"Máximo vendido: {np.max(cantidades)}")
        print(f"Mínimo vendido: {np.min(cantidades)}")

class GraficaBar(Reporte):
    def __init__(self, datos):
        self.datos = datos

    def mostrar(self):
        productos = [v[1] for v in self.datos]
        cantidades = [v[3] for v in self.datos]
        plt.bar(productos, cantidades)
        plt.title("Ventas por Producto")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad Vendida")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

class GraficaScatter(Reporte):
    def __init__(self, cursor):
        self.cursor = cursor

    def mostrar(self):
        self.cursor.execute("SELECT precio, cantidad FROM productos")
        datos = self.cursor.fetchall()
        precios = [d[0] for d in datos]
        cantidades = [d[1] for d in datos]
        plt.scatter(precios, cantidades)
        plt.title("Precio vs Cantidad")
        plt.xlabel("Precio")
        plt.ylabel("Cantidad")
        plt.grid(True)
        plt.show()

class GraficaPie(Reporte):
    def __init__(self, cursor):
        self.cursor = cursor

    def mostrar(self):
        self.cursor.execute("""
        SELECT categorias.nombre, COUNT(productos.id)
        FROM productos
        JOIN categorias ON productos.categoria_id = categorias.id
        GROUP BY categorias.nombre
        """)
        datos = self.cursor.fetchall()
        etiquetas = [d[0] for d in datos]
        valores = [d[1] for d in datos]
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')
        plt.title("Proporción por Categoría")
        plt.show()

# -----------------------------
# Programa principal
# -----------------------------
conexion, cursor = conectar_mysql()
crear_base_datos(cursor, conexion)

# Consultar ventas
cursor.execute("USE tienda_db")
cursor.execute("""
SELECT ventas.id, productos.nombre, ventas.fecha, ventas.cantidad_vendida
FROM ventas
JOIN productos ON ventas.producto_id = productos.id
""")
ventas = cursor.fetchall()

while True:
    print("\nMENÚ DE OPCIONES")
    print("1. Ver estadísticas básicas")
    print("2. Ver gráfica de ventas (bar)")
    print("3. Ver gráfica precio vs cantidad (scatter)")
    print("4. Ver gráfica por categoría (pie)")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        reporte = Estadistica(ventas)
    elif opcion == "2":
        reporte = GraficaBar(ventas)
    elif opcion == "3":
        reporte = GraficaScatter(cursor)
    elif opcion == "4":
        reporte = GraficaPie(cursor)
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
        continue

    reporte.mostrar()

cursor.close()
conexion.close()
print("Conexión cerrada correctamente.")