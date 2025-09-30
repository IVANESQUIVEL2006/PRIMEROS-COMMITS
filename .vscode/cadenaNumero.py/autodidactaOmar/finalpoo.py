# ---------------------------------------------
# MÓDULO DE INICIALIZACIÓN DE BASE DE DATOS
# Proyecto Final: Sistema de Análisis para Productos en una Tienda
# Autor: Jesús Iván Esquivel Ruiz
# ---------------------------------------------

# Importamos el módulo necesario para conectar Python con MySQL
import mysql.connector

# ---------------------------------------------
# 1. CONFIGURACIÓN DE CONEXIÓN
# ---------------------------------------------

# Definimos los datos de conexión al servidor MySQL
HOST = "localhost"       # Dirección del servidor (usualmente 'localhost' si es local)
USER = "root"            # Usuario con permisos para crear bases de datos
PASSWORD = "ROOT"        # Contraseña del usuario (debe coincidir con la configurada en MySQL)

# Establecemos la conexión inicial al servidor MySQL
# Nota: No seleccionamos aún una base de datos porque vamos a crearla
try:
    conexion = mysql.connector.connect(
        host=HOST,
        user="root",
        password="ROOT"
    )
    cursor = conexion.cursor()
    print("Conexión exitosa al servidor MySQL.")
except mysql.connector.Error as err:
    print(f"Error al conectar con MySQL: {err}")
    exit()

# ---------------------------------------------
# 2. SCRIPT SQL PARA CREAR LA BASE DE DATOS Y TABLAS
# ---------------------------------------------

# Este bloque contiene múltiples sentencias SQL:
# - Crear la base de datos
# - Crear las tablas: categorias, proveedores, productos, ventas
# - Insertar datos de ejemplo
script_sql = """
DROP DATABASE IF EXISTS tienda_db;
CREATE DATABASE IF NOT EXISTS tienda_db;
USE tienda_db;

CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cantidad_vendida INT NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

INSERT INTO categorias (nombre) VALUES  
('Electrónicos'),
('Ropa'),
('Alimentos'),
('Hogar'),
('Juguetes');

INSERT INTO proveedores (nombre, telefono) VALUES  
('TecnoSuministros', '555-100-2000'),
('ModaTotal', '555-100-3000'),
('AlimentosSA', '555-100-4000');

INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES  
('Laptop', 1200.00, 15, 1),
('Smartphone', 800.00, 30, 1),
('Camisa', 25.50, 50, 2),
('Arroz', 3.20, 100, 3),
('Sofá', 450.00, 5, 4),
('Muñeca', 15.75, 20, 5);

INSERT INTO ventas (producto_id, cantidad_vendida) VALUES  
(1, 2),
(2, 5),
(3, 10),
(4, 15),
(5, 1),
(6, 3),
(2, 4),
(3, 8),
(4, 20);
"""

# ---------------------------------------------
# 3. EJECUCIÓN DEL SCRIPT SQL
# ---------------------------------------------

# Ejecutamos cada sentencia SQL por separado
# Esto es necesario porque cursor.execute() no acepta múltiples sentencias juntas
try:
    for statement in script_sql.strip().split(";"):
        if statement.strip():  # Ignora líneas vacías
            cursor.execute(statement)
    conexion.commit()  # Confirma los cambios en la base de datos
    print("Base de datos y tablas creadas correctamente. Datos insertados.")
except mysql.connector.Error as err:
    # - La f"" es una f-string, que permite insertar el contenido de err directamente en el texto
    print(f"Error al ejecutar el script SQL: {err}")
    conexion.rollback()
    cursor.close()
    conexion.close()
    exit()

# ---------------------------------------------
# 4. CONSULTA JOIN PARA MOSTRAR VENTAS CON NOMBRE DE PRODUCTO
# ---------------------------------------------

# Esta consulta une las tablas 'ventas' y 'productos' para mostrar el nombre del producto vendido
consulta_join = """
USE tienda_db;
SELECT 
    ventas.id AS venta_id,
    productos.nombre AS nombre_producto,
    ventas.fecha,
    ventas.cantidad_vendida
FROM ventas
JOIN productos ON ventas.producto_id = productos.id;
"""

try:
    # el try 
    for statement in consulta_join.strip().split(";"):

        # verifica que le sentencia no este vacia
        # el strip se usa para limpiar una cadena de texto eliminando los espacios en blanco
        # el split se usa para dividir una cadena de texto en partes usando un separador el resultados una lista con cada fragmento
        if statement.strip():
            # es el metodo que envia la instruccion a la base de datos
            # no aspea multiples sentencias a la vez
          # cadena .split() se usa para dividir una cadena de texto en partes usando un separador el resultados una lista con cada fragmento
          # - Aquí el separador es la coma ,.
     

            cursor.execute(statement)

    resultados = cursor.fetchall()

#l n es un salto de linea
    print("\nVentas con nombre de producto:")
    for fila in resultados:
        # fila[0] = venta_id, fila[1] = nombre_producto, fila[2] = fecha, fila[3] = cantidad_vendida
        print(f"Venta ID: {fila[0]}, Producto: {fila[1]}, Fecha: {fila[2]}, Cantidad Vendida: {fila[3]}")

except mysql.connector.Error as err:
    print(f"Error al ejecutar la consulta JOIN: {err}")

# ---------------------------------------------
# 5. CIERRE DE CONEXIÓN
# ---------------------------------------------

# Cerramos el cursor y la conexión con el servidor MySQL
cursor.close()
conexion.close()
print("\nConexión cerrada correctamente.")

