# Importa las librerías necesarias.
import mysql.connector # Esta línea trae el conector de MySQL, que es como un "puente" entre tu código Python y la base de datos MySQL. Sin él, no podrías hablar con la base de datos.
import matplotlib.pyplot as plt # Importa la librería Matplotlib, específicamente el módulo `pyplot`, que es esencial para crear gráficos de manera sencilla (como barras o líneas).

# -----------------
## **Clase `BaseDatos`**
# -----------------
# Define la clase `BaseDatos`. En el mundo de la Programación Orientada a Objetos (POO), una clase es como un "molde" o un "plano" para crear objetos. En este caso, el molde es para crear objetos que manejen la conexión y las operaciones con la base de datos.
class BaseDatos:
    # Este es el método `__init__`, que es el "constructor" de la clase. Se ejecuta automáticamente cada vez que creas un nuevo objeto `BaseDatos`. Su trabajo es preparar el objeto con los datos iniciales.
    def __init__(self):
        # Estas líneas definen los atributos (o propiedades) del objeto. Son como variables internas del objeto.
        self.host = "localhost" # 'localhost' se refiere a tu propia computadora, donde está corriendo el servidor de la base de datos.
        self.user = "root" # 'root' es el usuario por defecto de MySQL con todos los permisos. Es importante cambiarlo en un entorno real.
        self.password = "ROOT" # La contraseña para el usuario 'root'.
        self.database = "TRABAJO FINAL POO" # El nombre de la base de datos a la que te vas a conectar.
        self.conexion = None # Inicializa la variable `conexion` como `None`. Esto significa que al principio no hay una conexión activa.
    
    # Este método se encarga de establecer la conexión con la base de datos usando los atributos definidos arriba.
    def conectar(self):
        try: # El bloque `try` intenta ejecutar el código que podría causar un error (como un fallo de conexión).
            # Aquí es donde realmente se establece la conexión. Llama a la función `connect` de la librería `mysql.connector` y le pasa los datos. El resultado se guarda en el atributo `self.conexion`.
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return True # Si la conexión se realiza sin problemas, devuelve `True` para indicar que todo salió bien.
        except Exception as e: # El bloque `except` se ejecuta si algo en el bloque `try` falló.
            print(f"Error de conexión: {e}") # Imprime un mensaje de error que incluye la descripción del problema (`e`).
            return False # Si la conexión falla, devuelve `False`.
    
    # Este método es la herramienta principal para interactuar con la base de datos. Sirve para enviar cualquier tipo de comando SQL.
    def ejecutar_query(self, query, params=None):
        try:
            cursor = self.conexion.cursor() # Crea un `cursor`. Un cursor es como un "puntero" o un "intermediario" que permite enviar comandos y recibir resultados de la base de datos.
            cursor.execute(query, params or ()) # Ejecuta la consulta SQL (`query`). Los `params` son los valores que se sustituyen de forma segura en la consulta (ej. `%s`). Si no hay `params`, usa una tupla vacía `()`.
            
            # Esta condición verifica si la consulta es un `SELECT` (es decir, una consulta para leer datos). La comprobación se hace con `.strip()`, `.lower()`, y `.startswith()` para que sea robusta.
            if query.strip().lower().startswith('select'):
                resultado = cursor.fetchall() # El método `fetchall()` trae todos los resultados de la consulta a la vez y los guarda en la variable `resultado`.
            else: # Si no es un `SELECT`, la consulta es para modificar la base de datos (INSERT, UPDATE, DELETE).
                self.conexion.commit() # El método `commit()` confirma los cambios hechos. Sin esto, los cambios no se guardan permanentemente en la base de datos.
                resultado = cursor.rowcount # `rowcount` devuelve el número de filas que fueron afectadas por la última operación.
            cursor.close() # Es una buena práctica cerrar el cursor una vez que terminaste de usarlo para liberar recursos.
            return resultado # Devuelve los resultados obtenidos.
        except Exception as e:
            print(f"Error en consulta: {e}") # Imprime un mensaje si la consulta tiene un error.
            return None # Devuelve `None` para indicar que no hubo un resultado válido.
    
    # Este método cierra la conexión a la base de datos. Es crucial para liberar los recursos del servidor.
    def cerrar(self):
        if self.conexion: # Verifica si la variable `self.conexion` no es `None`, lo que significa que hay una conexión activa.
            self.conexion.close() # Cierra la conexión.

# -----------------
## **Clase `Producto`**
# -----------------
# Esta clase es un "modelo" para representar un producto en Python. Ayuda a organizar la información de una fila de la tabla `productos` de la base de datos en un objeto.
class Producto:
    # El constructor de la clase `Producto`.
    def __init__(self, id, nombre, precio, cantidad, categoria_id):
        # Estas líneas asignan los valores pasados al crear el objeto a sus atributos correspondientes.
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria_id = categoria_id
    
    # Este método es para mostrar la información del producto de forma clara y legible.
    def mostrar(self):
        # `f-string` crea una cadena de texto formateada, donde las variables entre llaves `{}` se reemplazan por sus valores.
        return f"ID: {self.id}, {self.nombre}, ${self.precio}, Cantidad: {self.cantidad}"

# -----------------
## **Clase `Estadisticas`**
# -----------------
# Esta clase agrupa funciones para realizar cálculos estadísticos.
class Estadisticas:
    # `@staticmethod` indica que este es un método estático. Esto significa que puedes llamarlo sin necesidad de crear un objeto de la clase `Estadisticas`, como `Estadisticas.media_precios(...)`.
    @staticmethod
    def media_precios(productos):
        if not productos: # Si la lista de productos está vacía, no se puede calcular nada.
            return 0
        precios = [p[2] for p in productos] # Esta es una "comprensión de lista". Crea una nueva lista extrayendo el precio (el elemento en el índice `2`) de cada producto en la lista original.
        return sum(precios) / len(precios) # La suma de los precios dividida por el número de productos da el promedio.
    
    @staticmethod
    def max_min(productos):
        if not productos:
            return {"max": 0, "min": 0}
        precios = [p[2] for p in productos]
        return {"max": max(precios), "min": min(precios)} # Devuelve un diccionario con el precio más alto y el más bajo.
    
    @staticmethod
    def total_ventas(ventas):
        if not ventas:
            return 0
        return sum(v[1] for v in ventas) # Suma la cantidad vendida (segundo elemento de cada tupla de venta).

# -----------------
## **Función `main`**
# -----------------
# Esta es la función principal del programa. Es el punto de entrada y controla el flujo de la aplicación.
def main():
    db = BaseDatos() # Crea un objeto de la clase `BaseDatos`.
    if not db.conectar(): # Intenta conectar. Si devuelve `False`, el programa se detiene aquí.
        print("Error al conectar con la base de datos")
        return
    
    # El bucle `while True` crea un ciclo infinito que se repite hasta que el usuario decida salir.
    while True:
        # Imprime el menú de opciones.
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver todos los productos")
        print("2. Buscar productos por nombre (LIKE)")
        print("3. Productos por categoría")
        print("4. Productos por rango de precio")
        print("5. Ver estadísticas")
        print("6. Ver ventas por producto")
        print("7. Ver gráfico de precios")
        print("8. Ver gráfico de ventas")
        print("9. Salir")
        
        opcion = input("Elige una opción: ") # Le pide al usuario que ingrese un número.
        
        # Estas sentencias `if/elif/else` verifican qué opción eligió el usuario y ejecutan el código correspondiente.
        if opcion == "1":
            productos = db.ejecutar_query("SELECT * FROM productos") # Ejecuta la consulta para obtener todos los productos.
            if productos:
                for p in productos: # Itera sobre cada producto devuelto.
                    producto = Producto(p[0], p[1], p[2], p[3], p[4]) # Crea un objeto `Producto` a partir de los datos.
                    print(producto.mostrar()) # Llama al método `mostrar` del objeto para imprimir sus detalles.
            else:
                print("No hay productos")
        
        elif opcion == "2":
            nombre_buscar = input("Nombre a buscar: ")
            productos = db.ejecutar_query(
                "SELECT * FROM productos WHERE nombre LIKE %s", # La cláusula `LIKE %s` busca nombres que contengan el texto.
                (f"%{nombre_buscar}%",) # `f"%{...}%"` crea una cadena para la búsqueda "LIKE", buscando el nombre en cualquier parte del texto.
            )
            if productos:
                for p in productos:
                    producto = Producto(p[0], p[1], p[2], p[3], p[4])
                    print(producto.mostrar())
            else:
                print("No se encontraron productos")
        
        elif opcion == "3":
            print("Categorías disponibles:")
            categorias = db.ejecutar_query("SELECT * FROM categorias")
            if categorias:
                for cat in categorias:
                    print(f"{cat[0]}. {cat[1]}")
            categoria_id = input("ID de categoría: ")
            productos = db.ejecutar_query(
                "SELECT * FROM productos WHERE categoria_id = %s", # Busca productos por un ID de categoría específico.
                (categoria_id,)
            )
            if productos:
                for p in productos:
                    producto = Producto(p[0], p[1], p[2], p[3], p[4])
                    print(producto.mostrar())
            else:
                print("No hay productos en esta categoría")
        
        elif opcion == "4":
            min_precio = input("Precio mínimo: ")
            max_precio = input("Precio máximo: ")
            productos = db.ejecutar_query(
                "SELECT * FROM productos WHERE precio BETWEEN %s AND %s", # Busca productos en un rango de precio.
                (min_precio, max_precio)
            )
            if productos:
                for p in productos:
                    producto = Producto(p[0], p[1], p[2], p[3], p[4])
                    print(producto.mostrar())
            else:
                print("No hay productos en este rango de precio")
        
        elif opcion == "5":
            productos = db.ejecutar_query("SELECT * FROM productos")
            ventas = db.ejecutar_query("SELECT * FROM ventas")
            
            if productos:
                stats = Estadisticas() # No es estrictamente necesario crear un objeto, pero es una forma válida de llamar a los métodos estáticos.
                media = stats.media_precios(productos)
                max_min = stats.max_min(productos)
                total_ventas = stats.total_ventas(ventas) if ventas else 0
                
                print(f"Precio promedio: ${media:.2f}") # El `.2f` formatea el número a dos decimales.
                print(f"Precio más alto: ${max_min['max']:.2f}")
                print(f"Precio más baja: ${max_min['min']:.2f}")
                print(f"Total de ventas: {total_ventas} unidades")
            else:
                print("No hay datos para estadísticas")
        
        elif opcion == "6":
            ventas = db.ejecutar_query("""
                SELECT p.nombre, SUM(v.cantidad_vendida) as total_vendido
                FROM ventas v
                JOIN productos p ON v.producto_id = p.id
                GROUP BY p.nombre
                ORDER BY total_vendido DESC
            """)
            if ventas:
                print("Ventas por producto:")
                for v in ventas:
                    print(f"{v[0]}: {v[1]} unidades vendidas")
            else:
                print("No hay datos de ventas")
        
        elif opcion == "7":
            productos = db.ejecutar_query("SELECT * FROM productos")
            if productos:
                nombres = [p[1] for p in productos]
                precios = [p[2] for p in productos]
                
                plt.bar(nombres, precios) # La función `plt.bar` crea un gráfico de barras.
                plt.title("Precios de Productos")
                plt.ylabel("Precio ($)")
                plt.xticks(rotation=45) # Rota las etiquetas del eje X 45 grados para que no se superpongan si los nombres son largos.
                plt.tight_layout() # Ajusta automáticamente el gráfico para que todo quepa bien.
                plt.show() # Muestra la ventana con el gráfico. 
            else:
                print("No hay productos para graficar")
        
        elif opcion == "8":
            ventas = db.ejecutar_query("""
                SELECT p.nombre, SUM(v.cantidad_vendida) as total_vendido
                FROM ventas v
                JOIN productos p ON v.producto_id = p.id
                GROUP BY p.nombre
            """)
            if ventas:
                nombres = [v[0] for v in ventas]
                cantidades = [v[1] for v in ventas]
                
                plt.bar(nombres, cantidades)
                plt.title("Ventas por Producto")
                plt.ylabel("Unidades vendidas")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
                
            else:
                print("No hay datos de ventas para graficar")
        
        elif opcion == "9":
            print("¡Adiós!")
            break # La palabra clave `break` saca al programa del bucle `while`.
        
        else:
            print("Opción no válida")
    
    db.cerrar() # Esta línea se ejecuta una vez que el bucle ha terminado (cuando el usuario elige la opción 9), asegurándose de que la conexión a la base de datos se cierre de manera segura.

# -----------------
## **Punto de Entrada del Programa**
# -----------------
# Esta línea de código es un estándar en Python.
if __name__ ==  "__main__":
    main() # Si el script se ejecuta directamente (no se importa como un módulo), llama a la función `main` para que todo el programa comience.