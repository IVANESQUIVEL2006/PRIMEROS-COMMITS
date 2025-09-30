from datetime import datetime

class Producto:
    def __init__(self, nombre="", precio_base=0, stock=0):
        self.nombre = nombre
        self._precio_base = precio_base
        self._stock = stock
        self.ultima_actualizacion = datetime.now()
    
    @property
    def precio_base(self):
        return self._precio_base
    
    @precio_base.setter
    def precio_base(self, valor):
        if valor < 0:
            print("Error: El precio no puede ser negativo")
            return
        self._precio_base = valor
        self.actualizar_fecha()
    
    @property
    def precio_con_iva(self):
        return self._precio_base * 1.16  # IVA del 16%
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, cantidad):
        if cantidad < 0:
            print("Error al asignar stock negativo")
            return
        self._stock = cantidad
        self.actualizar_fecha()
    
    def actualizar_fecha(self):
        self.ultima_actualizacion = datetime.now()
    
    def mostrar_info(self):
        print("\n--- Información del Producto ---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio base: ${self.precio_base:.2f}")
        print(f"Precio con IVA (16%): ${self.precio_con_iva:.2f}")
        print(f"Stock disponible: {self.stock}")
        print(f"Última actualización: {self.ultima_actualizacion}")
        print("-------------------------------")

def menu():
    print("\n=== MENÚ DE INVENTARIO ===")
    print("1. Crear nuevo producto")
    print("2. Modificar precio base")
    print("3. Modificar stock")
    print("4. Ver información del producto")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

# Programa principal
producto = None

while True:
    opcion = menu()
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio base: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        producto = Producto(nombre, precio, stock)
        print("\n¡Producto creado exitosamente!")
    
    elif opcion == "2":
        if producto:
            nuevo_precio = float(input("Ingrese el nuevo precio base: "))
            producto.precio_base = nuevo_precio
        else:
            print("Primero debe crear un producto")
    
    elif opcion == "3":
        if producto:
            nuevo_stock = int(input("Ingrese la nueva cantidad en stock: "))
            producto.stock = nuevo_stock
        else:
            print("Primero debe crear un producto")
    
    elif opcion == "4":
        if producto:
            producto.mostrar_info()
        else:
            print("No hay producto creado aún")
    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
