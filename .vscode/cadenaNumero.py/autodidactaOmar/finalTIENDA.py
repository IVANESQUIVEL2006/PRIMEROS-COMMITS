import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt


# -------------------------------
# Clase para manejar la conexión
# -------------------------------
class ConexionMySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def __enter__(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.conexion

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conexion:
            self.conexion.close()


# -------------------------------
# Clases de Productos
# -------------------------------
class Producto:
    def __init__(self, nombre, precio, cantidad, categoria_id):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria_id = categoria_id

    def guardar(self, conexion):
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.nombre, self.precio, self.cantidad, self.categoria_id))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al guardar producto: {e}")
            return False

    def mostrar(self):
        return f"{self.nombre} | ${self.precio:.2f} | Cant: {self.cantidad}"


class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, categoria_id, garantia, voltaje):
        super().__init__(nombre, precio, cantidad, categoria_id)
        self.garantia = garantia
        self.voltaje = voltaje

    def guardar(self, conexion):
        try:
            cursor = conexion.cursor()
            query = """INSERT INTO productos 
                       (nombre, precio, cantidad, categoria_id, garantia, voltaje) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (self.nombre, self.precio, self.cantidad, self.categoria_id,
                                   self.garantia, self.voltaje))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al guardar producto electrónico: {e}")
            return False

    def mostrar(self):
        return f"{self.nombre} | ${self.precio:.2f} | Cant: {self.cantidad} | Garantía: {self.garantia} meses | Voltaje: {self.voltaje}V"


# -------------------------------
# Clase para manejar productos
# -------------------------------
class GestorProductos:
    def __init__(self, conexion):
        self.conexion = conexion

    def buscar_simple(self):
        cursor = self.conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

    def buscar_avanzada(self, categoria=None, nombre=None, precio_min=None, precio_max=None):
        query = """SELECT p.*, c.nombre AS categoria_nombre 
                   FROM productos p 
                   LEFT JOIN categorias c ON p.categoria_id = c.id 
                   WHERE 1=1"""
        params = []

        if categoria:
            query += " AND c.nombre LIKE %s"
            params.append(f"%{categoria}%")
        if nombre:
            query += " AND p.nombre LIKE %s"
            params.append(f"%{nombre}%")
        if precio_min is not None:
            query += " AND p.precio >= %s"
            params.append(precio_min)
        if precio_max is not None:
            query += " AND p.precio <= %s"
            params.append(precio_max)

        cursor = self.conexion.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()

    def obtener_ventas_por_producto(self):
        cursor = self.conexion.cursor(dictionary=True)
        query = """SELECT p.id, p.nombre, SUM(v.cantidad_vendida) AS total_vendido
                   FROM productos p
                   LEFT JOIN ventas v ON p.id = v.producto_id
                   GROUP BY p.id, p.nombre"""
        cursor.execute(query)
        return cursor.fetchall()

    def obtener_productos_por_categoria(self):
        cursor = self.conexion.cursor(dictionary=True)
        query = """SELECT c.nombre AS categoria, COUNT(p.id) AS total 
                   FROM categorias c
                   LEFT JOIN productos p ON p.categoria_id = c.id
                   GROUP BY c.id"""
        cursor.execute(query)
        return cursor.fetchall()


# -------------------------------
# Clase de estadísticas
# -------------------------------
class EstadisticaProductos:
    def __init__(self, productos):
        self.productos = productos

    def generar_reporte(self, ventas):
        precios = [float(p['precio']) for p in self.productos] if self.productos else [0]
        cantidades = [int(p['cantidad']) for p in self.productos] if self.productos else [0]

        reporte = {
            "media_precios": sum(precios) / len(precios) if precios else 0,
            "max_precio": max(precios) if precios else 0,
            "min_precio": min(precios) if precios else 0,
            "total_productos": len(self.productos),
            "promedio_ventas": sum(v.get("total_vendido", 0) for v in ventas) / len(ventas) if ventas else 0
        }
        return reporte


# -------------------------------
# Clase para gráficos
# -------------------------------
class Graficador:
    @staticmethod
    def grafico_barras_ventas(ventas):
        nombres = [v['nombre'] for v in ventas]
        cantidades = [v.get('total_vendido', 0) for v in ventas]

        plt.bar(nombres, cantidades)
        plt.title("Ventas por producto")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad vendida")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def grafico_dispersion_precio_cantidad(productos):
        precios = [float(p['precio']) for p in productos]
        cantidades = [int(p['cantidad']) for p in productos]

        plt.scatter(precios, cantidades)
        plt.title("Precio vs Cantidad")
        plt.xlabel("Precio")
        plt.ylabel("Cantidad")
        plt.show()

    @staticmethod
    def grafico_pastele_categorias(datos):
        categorias = [d['categoria'] for d in datos]
        totales = [d['total'] for d in datos]

        plt.pie(totales, labels=categorias, autopct="%1.1f%%")
        plt.title("Productos por categoría")
        plt.show()
