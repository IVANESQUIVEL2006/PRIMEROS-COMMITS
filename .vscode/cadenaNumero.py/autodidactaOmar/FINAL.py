import mysql.connector
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import numpy as np
from datetime import datetime

# -------------------
# CONFIGURACIÓN
# -------------------
HOST = "localhost"
USER = "root"
PASSWORD = "ROOT"  # Cambia por tu contraseña de MySQL
DB = "tienda_db"

# -------------------
# CLASES ABSTRACTAS
# -------------------
class Graficador(ABC):
    @abstractmethod
    def generar_grafica(self, datos, titulo):
        pass
    
    def mostrar_grafica(self):
        plt.tight_layout()
        plt.show()
        
    def guardar_grafica(self, nombre_archivo):
        plt.savefig(nombre_archivo)
        print(f"Gráfica guardada como {nombre_archivo}")

class OperacionBD(ABC):
    @abstractmethod
    def ejecutar(self, cursor, conexion):
        pass

# -------------------
# GRAFICADORES CONCRETOS
# -------------------
class GraficoBarras(Graficador):
    def generar_grafica(self, datos, titulo="Ventas por Producto"):
        productos = [item[0] for item in datos]
        valores = [item[1] for item in datos]
        
        plt.figure(figsize=(12, 6))
        barras = plt.bar(productos, valores, color='skyblue')
        plt.title(titulo, fontsize=14, fontweight='bold')
        plt.xlabel('Productos')
        plt.ylabel('Valores')
        plt.xticks(rotation=45, ha='right')
        
        for barra, valor in zip(barras, valores):
            plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.05,
                    f'{valor:.2f}', ha='center', va='bottom')

class GraficoDispersion(Graficador):
    def generar_grafica(self, datos, titulo="Precios vs Cantidad"):
        precios = [item[0] for item in datos]
        cantidades = [item[1] for item in datos]
        productos = [item[2] for item in datos]
        
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(precios, cantidades, s=100, alpha=0.7, c=np.random.rand(len(precios)), cmap='viridis')
        
        for i, producto in enumerate(productos):
            plt.annotate(producto, (precios[i], cantidades[i]), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8)
        
        plt.title(titulo, fontsize=14, fontweight='bold')
        plt.xlabel('Precio ($)')
        plt.ylabel('Cantidad')
        plt.grid(True, alpha=0.3)
        plt.colorbar(scatter, label='Intensidad')

class GraficoTorta(Graficador):
    def generar_grafica(self, datos, titulo="Proporción por Categoría"):
        categorias = [item[0] for item in datos]
        valores = [item[1] for item in datos]
        
        umbral = 0.02 * sum(valores)
        categorias_filtradas = []
        valores_filtrados = []
        otros = 0
        
        for cat, val in zip(categorias, valores):
            if val >= umbral:
                categorias_filtradas.append(cat)
                valores_filtrados.append(val)
            else:
                otros += val
                
        if otros > 0:
            categorias_filtradas.append("Otros")
            valores_filtrados.append(otros)
        
        plt.figure(figsize=(10, 8))
        plt.pie(valores_filtrados, labels=categorias_filtradas, autopct='%1.1f%%', 
                startangle=90, colors=plt.cm.Set3(np.linspace(0, 1, len(valores_filtrados))))
        plt.title(titulo, fontsize=14, fontweight='bold')
        plt.axis('equal')

# -------------------
# OPERACIONES BD CONCRETAS
# -------------------
class ObtenerVentasPorProducto(OperacionBD):
    def ejecutar(self, cursor, conexion):
        cursor.execute("""
            SELECT nombre, precio * cantidad as ventas 
            FROM productos 
            ORDER BY ventas DESC
        """)
        return cursor.fetchall()

class ObtenerPreciosYCantidades(OperacionBD):
    def ejecutar(self, cursor, conexion):
        cursor.execute("SELECT precio, cantidad, nombre FROM productos ORDER BY nombre")
        return cursor.fetchall()

class ObtenerProporcionCategorias(OperacionBD):
    def ejecutar(self, cursor, conexion):
        cursor.execute("""
            SELECT c.nombre, SUM(p.precio * p.cantidad) as total_ventas
            FROM categorias c
            JOIN producto_categoria pc ON c.id = pc.categoria_id
            JOIN productos p ON pc.producto_id = p.id
            GROUP BY c.id, c.nombre
            ORDER BY total_ventas DESC
        """)
        return cursor.fetchall()

class ObtenerProductosPorCategoria(OperacionBD):
    def ejecutar(self, cursor, conexion):
        cursor.execute("""
            SELECT c.nombre as categoria, 
                   GROUP_CONCAT(p.nombre SEPARATOR ', ') as productos,
                   COUNT(p.id) as cantidad_productos
            FROM categorias c
            JOIN producto_categoria pc ON c.id = pc.categoria_id
            JOIN productos p ON pc.producto_id = p.id
            GROUP BY c.id, c.nombre
            ORDER BY cantidad_productos DESC
        """)
        return cursor.fetchall()

# -------------------
# FACHADA PARA GESTIÓN DE GRÁFICOS
# -------------------
class GestorGraficos:
    def __init__(self, cursor, conexion):
        self.cursor = cursor
        self.conexion = conexion
    
    def generar_grafico_ventas(self):
        operacion = ObtenerVentasPorProducto()
        datos = operacion.ejecutar(self.cursor, self.conexion)
        
        graficador = GraficoBarras()
        graficador.generar_grafica(datos, "Ventas Totales por Producto (Precio x Cantidad)")
        graficador.mostrar_grafica()
    
    def generar_grafico_dispersion(self):
        operacion = ObtenerPreciosYCantidades()
        datos = operacion.ejecutar(self.cursor, self.conexion)
        
        graficador = GraficoDispersion()
        graficador.generar_grafica(datos, "Relación Precio vs Cantidad por Producto")
        graficador.mostrar_grafica()
    
    def generar_grafico_torta(self):
        operacion = ObtenerProporcionCategorias()
        datos = operacion.ejecutar(self.cursor, self.conexion)
        
        graficador = GraficoTorta()
        graficador.generar_grafica(datos, "Distribución de Ventas por Categoría")
        graficador.mostrar_grafica()

# -------------------
# CONEXIÓN Y VERIFICACIÓN
# -------------------
def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB
        )
        cursor = conexion.cursor()
        print("✅ Conexión exitosa a MySQL y base de datos tienda_db.")
        return conexion, cursor
    except mysql.connector.Error as err:
        print(f"❌ Error de conexión: {err}")
        print("💡 Asegúrate de:")
        print("   1. Tener MySQL instalado y funcionando")
        print("   2. Ejecutar el archivo tienda_db_setup.sql en MySQL Workbench primero")
        print("   3. Verificar usuario y contraseña en la configuración")
        exit()

def verificar_estructura(cursor):
    """Verifica que las tablas necesarias existan"""
    tablas_requeridas = ['productos', 'categorias', 'producto_categoria']
    for tabla in tablas_requeridas:
        cursor.execute(f"SHOW TABLES LIKE '{tabla}'")
        if not cursor.fetchone():
            print(f"❌ Error: La tabla '{tabla}' no existe en la base de datos")
            print("💡 Ejecuta el archivo tienda_db_setup.sql en MySQL Workbench primero")
            return False
    return True

# -------------------
# FUNCIONES DE MENÚ
# -------------------
def listar_productos(cursor):
    cursor.execute("""
        SELECT p.id, p.nombre, p.precio, p.cantidad, 
               GROUP_CONCAT(c.nombre SEPARATOR ', ') as categorias
        FROM productos p
        LEFT JOIN producto_categoria pc ON p.id = pc.producto_id
        LEFT JOIN categorias c ON pc.categoria_id = c.id
        GROUP BY p.id
        ORDER BY p.nombre
    """)
    productos = cursor.fetchall()
    if productos:
        print("\n--- LISTA DE PRODUCTOS ---")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Precio: ${p[2]}, Cantidad: {p[3]}, Categorías: {p[4]}")
    else:
        print("No hay productos registrados.")

def listar_categorias(cursor):
    cursor.execute("""
        SELECT c.id, c.nombre, c.descripcion, 
               COUNT(pc.producto_id) as cantidad_productos
        FROM categorias c
        LEFT JOIN producto_categoria pc ON c.id = pc.categoria_id
        GROUP BY c.id
        ORDER BY c.nombre
    """)
    categorias = cursor.fetchall()
    if categorias:
        print("\n--- LISTA DE CATEGORÍAS ---")
        for c in categorias:
            print(f"ID: {c[0]}, Nombre: {c[1]}, Descripción: {c[2]}, Productos: {c[3]}")
    else:
        print("No hay categorías registradas.")

def buscar_producto(cursor):
    nombre = input("Nombre del producto a buscar: ")
    cursor.execute("""
        SELECT p.id, p.nombre, p.precio, p.cantidad, 
               GROUP_CONCAT(c.nombre SEPARATOR ', ') as categorias
        FROM productos p
        LEFT JOIN producto_categoria pc ON p.id = pc.producto_id
        LEFT JOIN categorias c ON pc.categoria_id = c.id
        WHERE p.nombre LIKE %s
        GROUP BY p.id
    """, ("%" + nombre + "%",))
    resultados = cursor.fetchall()
    if resultados:
        print("\n--- PRODUCTOS ENCONTRADOS ---")
        for p in resultados:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Precio: ${p[2]}, Cantidad: {p[3]}, Categorías: {p[4]}")
    else:
        print("No se encontró el producto.")

# -------------------
# MENÚ PRINCIPAL
# -------------------
if __name__ == "__main__":
    try:
        conexion, cursor = conectar_mysql()
        
        if not verificar_estructura(cursor):
            exit()
            
        gestor_graficos = GestorGraficos(cursor, conexion)

        while True:
            print("\n===== SISTEMA DE GESTIÓN DE TIENDA =====")
            print("1. Listar productos")
            print("2. Listar categorías")
            print("3. Buscar producto")
            print("4. Gráfico de barras: Ventas por producto")
            print("5. Scatter Plot: Precios vs cantidad")
            print("6. Pie chart: Proporción por categoría")
            print("7. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                listar_productos(cursor)
            elif opcion == "2":
                listar_categorias(cursor)
            elif opcion == "3":
                buscar_producto(cursor)
            elif opcion == "4":
                gestor_graficos.generar_grafico_ventas()
            elif opcion == "5":
                gestor_graficos.generar_grafico_dispersion()
            elif opcion == "6":
                gestor_graficos.generar_grafico_torta()
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")

    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conexion' in locals() and conexion:
            conexion.close()
        print("Conexión cerrada correctamente.")