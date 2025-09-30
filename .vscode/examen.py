import matplotlib.pyplot as plt
import statistics as stat
import math

class Calculadora:
    def __init__(self, datos):
        self.datos = datos
        self.media = self.calcular_media()
        self.mediana = self.calcular_mediana()
        self.moda = self.calcular_moda()

    def calcular_media(self):
        return sum(self.datos) / len(self.datos)

    def calcular_mediana(self):
        datos_ordenados = sorted(self.datos)
        n = len(datos_ordenados)
        if n % 2 == 0:
            return (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
        else:
            return datos_ordenados[n // 2]
    
    def calcular_moda(self):
        frecuencias = {}
        for num in self.datos:
            if num in frecuencias:
                frecuencias[num] += 1
                
            else:
                frecuencias[num] = 1
        return max(frecuencias, key=frecuencias.get)
    
    def graficar(self, x, y):
        plt.plot(x, y, marker='o')
        plt.title("Gráfica de Datos")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
        
    def calcular(self):
        pass
    
    def __str__(self):
        return f"Media: {self.media}\Mediana: {self.mediana}\Modda: {self.moda}"

class OperacionesBasicas(Calculadora):
    def __init__(self, datos):
        super().__init__(datos)

    def suma(self):
        return sum(self.datos)

    def resta(self):
        resultado = self.datos[0]
        for num in self.datos[1:]:
            resultado -= num
        return resultado

    def multiplicacion(self):
        resultado = 1
        for num in self.datos:
            resultado *= num
        return resultado
    
    def division(self):
        resultado = self.datos[0]
        for num in self.datos[1:]:
            if num != 0:
                resultado /= num
                
            else:

             return "Error: división por cero"

                    
        return resultado
    
    def calcular(self):
        print(self)
        

class Estadisticas(Calculadora):
    def __init__(self, datos):
        super().__init__(datos)

    def calcular(self):
        media = self.calcular_media()
        mediana = self.calcular_mediana()
        moda = self.calcular_moda()
        print(self)
        return media, mediana, moda
        
class Graficador:
    def graficar(self, x, y):
        plt.plot(x, y, marker='o')
        plt.title("Gráfica de Datos")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
        
# Ejemplo de uso
datos = [10, 20, 30, 40, 50]

# Operaciones básicas
basico = OperacionesBasicas(datos)
print("Suma:", basico.suma())
print("Resta:", basico.resta())
print("Multiplicación:", basico.multiplicacion())
print("División:", basico.division())

# Estadísticas
estadistica = Estadisticas(datos)
media, mediana, moda = estadistica.calcular()
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Gráfica
x = [1, 2, 3, 4, 5]
y = datos
grafico = Graficador()
grafico.graficar(x, y)                              