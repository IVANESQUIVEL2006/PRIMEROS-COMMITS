import datetime
import functools

# ----------------- Decorador -----------------
def registro_llamada(func):
    """
    Este decorador imprime el nombre de la función antes de ejecutarla.
    Ayuda a ver el orden en que se llaman las funciones.
    """
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        print(f"--- Llamando a la función: {func.__name__} ---")
        return func(*args, **kwargs)
    return envoltura

# ----------------- Clase de Nómina -----------------
class Nomina:
    """
    Clase para gestionar los datos y cálculos de la nómina de los empleados.
    """
    def __init__(self):
        # Una lista donde guardaremos la información de cada empleado como un diccionario.
        self.empleados = []

    @registro_llamada
    def solicitar_datos(self):
        """
        Pide los datos de 5 empleados y los guarda.
        """
        for i in range(5):
            print(f"\n--- Ingreso de datos del Empleado {i + 1} ---")
            empleado = {}
            empleado['nombre'] = input("Nombre: ")
            empleado['apellido'] = input("Apellido: ")
            empleado['sueldo_base'] = float(input("Sueldo base: "))
            
            while True:
                tipo_isr_input = input("Tipo de ISR (1 para 8.3%, 2 para 10%): ")
                if tipo_isr_input in ['1', '2']:
                    empleado['tipo_isr'] = int(tipo_isr_input)
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            
            fecha_ingreso_str = input("Fecha de ingreso (AAAA-MM-DD): ")
            empleado['fecha_ingreso'] = datetime.datetime.strptime(fecha_ingreso_str, "%Y-%m-%d").date()
            empleado['num_hijos'] = int(input("Número de hijos: "))
            self.empleados.append(empleado)

    @registro_llamada
    def calcular_y_mostrar(self):
        """
        Calcula la nómina de todos los empleados y muestra el desglose y los promedios.
        """
        total_imss = 0
        total_isr = 0
        total_sueldo_neto = 0

        for emp in self.empleados:
            # Calcular la antigüedad en meses.
            meses_trabajados = (datetime.date.today().year - emp['fecha_ingreso'].year) * 12 + datetime.date.today().month - emp['fecha_ingreso'].month
            
            # Calcular la base imponible sumando bonificación y asignación familiar.
            bonificacion = emp['sueldo_base'] * 0.025 * meses_trabajados
            asignacion_familiar = emp['sueldo_base'] * 0.05 * emp['num_hijos']
            base_imponible = emp['sueldo_base'] + bonificacion + asignacion_familiar
            
            # Calcular descuentos de IMSS e ISR.
            descuento_imss = base_imponible * 0.07
            if emp['tipo_isr'] == 1:
                descuento_isr = base_imponible * 0.083
            else:
                descuento_isr = base_imponible * 0.10
            
            # Calcular el sueldo neto final.
            sueldo_neto = base_imponible - descuento_imss - descuento_isr
            
            # Acumular los totales.
            total_imss += descuento_imss
            total_isr += descuento_isr
            total_sueldo_neto += sueldo_neto
            
            # Mostrar el desglose individual.
            print(f"\n--- Nómina de {emp['nombre']} {emp['apellido']} ---")
            print(f"Base Imponible: ${base_imponible:,.2f}")
            print(f"Descuento IMSS: ${descuento_imss:,.2f}")
            print(f"Descuento ISR: ${descuento_isr:,.2f}")
            print(f"Sueldo Neto: ${sueldo_neto:,.2f}")

        # Mostrar los totales de la empresa.
        print("\n--- Resumen de la Empresa ---")
        print(f"Total a pagar de IMSS: ${total_imss:,.2f}")
        print(f"Total a pagar de ISR: ${total_isr:,.2f}")
        
        # Calcular y mostrar los promedios.
        if self.empleados: # Verifica que la lista no esté vacía.
            num_empleados = len(self.empleados)
            print(f"\n--- Promedios de Pago ---")
            print(f"Promedio de Sueldo Neto: ${total_sueldo_neto / num_empleados:,.2f}")
            print(f"Promedio de Descuento IMSS: ${total_imss / num_empleados:,.2f}")
            print(f"Promedio de Descuento ISR: ${total_isr / num_empleados:,.2f}")

# ----------------- Lógica Principal (Main) -----------------
if __name__ == "__main__":
    nomina_app = Nomina()
    nomina_app.solicitar_datos()
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver desglose de nómina y promedios")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case '1':
                # Al seleccionar esta opción, se hacen todos los cálculos y se muestran.
                nomina_app.calcular_y_mostrar()
            case '2':
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")