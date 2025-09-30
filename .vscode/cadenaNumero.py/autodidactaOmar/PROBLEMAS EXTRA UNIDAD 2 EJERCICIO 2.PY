# esta es una clase que nos permite trabajar con fechas y horas
from datetime import datetime

class Producto:
    IVA = 0.16  # 16% de IVA

    def __init__(self, nombre, precio_base=0, stock=0):
        self.nombre = nombre
        self._precio_base = None
        self._stock = None
        self.ultima_actualizacion = None
        self.precio_base = precio_base  # llama al setter
        self.stock = stock              # llama al setter

    # Precio base
    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        #se usa para verificar si un numer es negativo o no 
        if valor < 0:
            raise ValueError("Error: precio no puede ser negativo")
        self._precio_base = valor
        # sirve para registrar la fecha y hora exacta en que se hizo cambio en el objeto 
        self.ultima_actualizacion = datetime.now()

    # Stock
    @property
    def stock(self):
        return self._stock

    @stock.setter
    # permite asignar un valor al stock y si es negativo lanza un error
    def stock(self, valor):
        if valor < 0:
            raise ValueError("Error: stock no puede ser negativo")
        self._stock = valor
        self.ultima_actualizacion = datetime.now()

    # Precio con IVA calculado automáticamente
    @property
    def precio_con_iva(self):
        # verifica que el precio base tenga un valor asignado
        if self._precio_base is not None:
            # aqui es donde calculamos el precio con IVA
            #ecio_base * (1 + self.IVA)





            #Multiplica el precio base por 1 + IVA.
            #self.IVA es el porcentaje de IVA, por ejemplo 0.16 (16%).
           # Ejemplo: si _precio_base = 15000 →
            return round(self._precio_base * (1 + self.IVA), 2)
        return 0

producto = Producto("Laptop", 15000, 10)
print(f"Precio base: ${producto.precio_base} → Precio con IVA: ${producto.precio_con_iva}")
print(f"Stock actual: {producto.stock} → Última actualización: {producto.ultima_actualizacion}")

# Probar error al asignar stock negativo
# try intenta ejecutar el codigo y si falla lanza un error
try:
    # aqui como el 5 es menor que 0 lanza un error
    producto.stock = -5
    # captura el error y  evita que el programa se detenga
except Exception as e:
    # lo guarda en una variable y lo imprime
    print(e)
