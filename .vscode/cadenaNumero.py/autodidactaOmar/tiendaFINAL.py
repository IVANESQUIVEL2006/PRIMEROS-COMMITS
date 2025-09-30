from finalTIENDA import (
    ConexionMySQL, GestorProductos, Producto,
    ProductoElectronico, EstadisticaProductos, Graficador
)

# Configuración de conexión a MySQL
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "ROOT"   # cámbialo por tu contraseña real
DB_NAME = "tienda_analisis"


def main():
    while True:
        print("\n--- SISTEMA DE ANÁLISIS DE PRODUCTOS ---")
        print("1. Ver todos los productos")
        print("2. Búsqueda avanzada (categoría, nombre, precio)")
        print("3. Estadísticas de productos")
        print("4. Graficar datos")
        print("5. Agregar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            with ConexionMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) as conexion:
                gestor = GestorProductos(conexion)
                productos = gestor.buscar_simple()
                if productos:
                    for p in productos:
                        print(f"ID: {p['id']} | {p['nombre']} | ${float(p['precio']):.2f} | Cant: {p['cantidad']}")
                else:
                    print("No se encontraron productos.")

        elif opcion == "2":
            categoria = input("Categoría (dejar vacío para omitir): ").strip() or None
            nombre = input("Nombre (dejar vacío para omitir): ").strip() or None
            precio_min = input("Precio mínimo (dejar vacío para omitir): ").strip()
            precio_max = input("Precio máximo (dejar vacío para omitir): ").strip()
            precio_min = float(precio_min) if precio_min else None
            precio_max = float(precio_max) if precio_max else None

            with ConexionMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) as conexion:
                gestor = GestorProductos(conexion)
                resultados = gestor.buscar_avanzada(
                    categoria=categoria, nombre=nombre,
                    precio_min=precio_min, precio_max=precio_max
                )
                if resultados:
                    for r in resultados:
                        print(f"{r['id']} | {r['nombre']} | ${float(r['precio']):.2f} | Cant: {r['cantidad']} | Cat: {r.get('categoria_nombre','N/A')}")
                else:
                    print("No se encontraron resultados con esos criterios.")

        elif opcion == "3":
            with ConexionMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) as conexion:
                gestor = GestorProductos(conexion)
                productos = gestor.buscar_simple()
                ventas = gestor.obtener_ventas_por_producto()
                estad = EstadisticaProductos(productos)
                reporte = estad.generar_reporte(ventas)

                print("\n--- REPORTE ---")
                print(f"Media de precios: ${reporte['media_precios']:.2f}")
                print(f"Precio máximo: ${reporte['max_precio']:.2f}")
                print(f"Precio mínimo: ${reporte['min_precio']:.2f}")
                print(f"Total de productos: {reporte['total_productos']}")
                print(f"Promedio de ventas por producto: {reporte['promedio_ventas']:.2f}")
                print("\nVentas por producto:")
                for v in ventas:
                    print(f"{v['nombre']}: {v.get('total_vendido',0)} unidades")

        elif opcion == "4":
            print("1. Barras (Ventas por producto)")
            print("2. Dispersión (Precio vs Cantidad)")
            print("3. Pastel (Productos por categoría)")
            g = input("Elige gráfico: ").strip()

            with ConexionMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) as conexion:
                gestor = GestorProductos(conexion)
                if g == "1":
                    Graficador.grafico_barras_ventas(gestor.obtener_ventas_por_producto())
                elif g == "2":
                    Graficador.grafico_dispersion_precio_cantidad(gestor.buscar_simple())
                elif g == "3":
                    Graficador.grafico_pastele_categorias(gestor.obtener_productos_por_categoria())
                else:
                    print("Opción de gráfico inválida.")

        elif opcion == "5":
            print("1. Producto general")
            print("2. Producto electrónico")
            t = input("Tipo: ").strip()

            nombre = input("Nombre: ").strip()
            precio = float(input("Precio: ").strip())
            cantidad = int(input("Cantidad: ").strip())
            categoria_id = int(input("ID categoría: ").strip())

            with ConexionMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) as conexion:
                if t == "1":
                    prod = Producto(nombre, precio, cantidad, categoria_id)
                else:
                    garantia = int(input("Meses de garantía: ").strip())
                    voltaje = int(input("Voltaje: ").strip())
                    prod = ProductoElectronico(nombre, precio, cantidad, categoria_id, garantia, voltaje)

                if prod.guardar(conexion):
                    print("Producto guardado con éxito:")
                    print(prod.mostrar())
                else:
                    print("Error al guardar el producto.")

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta otra vez.")


if __name__ == "__main__":
    main()
