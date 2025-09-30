import math

class Movimiento:
    def mostrar_resultado(self, descripcion, valor, unidades):
        print(f"{descripcion}: {valor} {unidades}")

class MRU(Movimiento):
    def __init__(self):
        self.velocidad = float(input("Ingresa la velocidad (m/s): "))
        self.tiempo = float(input("Ingresa el tiempo (s): "))

    def calcular_distancia(self):
        distancia = self.velocidad * self.tiempo
        self.mostrar_resultado("Distancia recorrida (MRU)", distancia, "m")

class MRUA(Movimiento):
    def __init__(self):
        self.velocidad_inicial = float(input("Ingresa la velocidad inicial (m/s): "))
        self.aceleracion = float(input("Ingresa la aceleración (m/s²): "))
        self.tiempo = float(input("Ingresa el tiempo (s): "))

    def calcular_distancia(self):
        distancia = (self.velocidad_inicial * self.tiempo) + (0.5 * self.aceleracion * self.tiempo**2)
        self.mostrar_resultado("Distancia (MRUA)", distancia, "m")

    def calcular_velocidad_final(self):
        velocidad_final = self.velocidad_inicial + self.aceleracion * self.tiempo
        self.mostrar_resultado("Velocidad final", velocidad_final, "m/s")

class CaidaLibre(Movimiento):
    def __init__(self):
        self.altura = float(input("Ingresa la altura desde la que cae el objeto (m): "))
        self.g = 9.81

    def calcular_tiempo(self):
        tiempo = math.sqrt((2 * self.altura) / self.g)
        self.mostrar_resultado("Tiempo de caída", tiempo, "s")

    def calcular_velocidad_final(self):
        velocidad = math.sqrt(2 * self.g * self.altura)
        self.mostrar_resultado("Velocidad final al impactar", velocidad, "m/s")

class TiroParabolico(Movimiento):
    def __init__(self):
        self.velocidad_inicial = float(input("Ingresa la velocidad inicial (m/s): "))
        self.angulo = math.radians(float(input("Ingresa el ángulo de lanzamiento (grados): ")))
        self.g = 9.81

    def calcular_alcance(self):
        alcance = (self.velocidad_inicial**2 * math.sin(2 * self.angulo)) / self.g
        self.mostrar_resultado("Alcance horizontal", alcance, "m")

    def calcular_altura_maxima(self):
        altura = (self.velocidad_inicial**2 * math.sin(self.angulo)**2) / (2 * self.g)
        self.mostrar_resultado("Altura máxima", altura, "m")

    def calcular_tiempo_total(self):
        tiempo = (2 * self.velocidad_inicial * math.sin(self.angulo)) / self.g
        self.mostrar_resultado("Tiempo total de vuelo", tiempo, "s")

def menu():
    while True:
        print("\n=== Calculadora Científica de Física de Ivan ===")
        print("1. Movimiento Rectilíneo Uniforme (MRU)")
        print("2. Movimiento Uniformemente Acelerado (MRUA)")
        print("3. Caída Libre")
        print("4. Tiro Parabólico")
        print("5. Salir")
        opcion = input("Selecciona una opción compa (1-5): ")

        if opcion == "1":
            mru = MRU()
            mru.calcular_distancia()
        elif opcion == "2":
            mrua = MRUA()
            mrua.calcular_distancia()
            mrua.calcular_velocidad_final()
        elif opcion == "3":
            caida = CaidaLibre()
            caida.calcular_tiempo()
            caida.calcular_velocidad_final()
        elif opcion == "4":
            tiro = TiroParabolico()
            tiro.calcular_alcance()
            tiro.calcular_altura_maxima()
            tiro.calcular_tiempo_total()
        elif opcion == "5":
            print("Adiós we")
            break
        else:
            print("Opción no valida we. Intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()