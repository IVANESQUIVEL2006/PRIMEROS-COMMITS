import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Clase base abstracta
class AnalisisDatos:
    def __init__(self, datos):
        """Inicializa el objeto con los datos y crea un DataFrame."""
        self.datos = datos
        self.df = pd.DataFrame(datos, columns=['Valores'])

    def calcular_estadisticas(self):
        """Calcula estadísticas descriptivas."""
        return self.df.describe()

    def graficar_histograma(self):
        """Genera un histograma de los datos."""
        plt.hist(self.df['Valores'], bins=10, edgecolor='black')
        plt.title('Histograma de Valores')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.show()

    def graficar_diagrama_dispersion(self):
        """Genera un diagrama de dispersión para visualizar la distribución de los datos."""
        plt.scatter(range(len(self.datos)), self.datos, color='red', marker='o')
        plt.title('Diagrama de Dispersión')
        plt.xlabel('Índice')
        plt.ylabel('Valores')
        plt.show()

# Clase heredada con polimorfismo
class EstadisticaDescriptiva(AnalisisDatos):
    def __init__(self, datos):
        """Inicializa la clase hija llamando al constructor de la clase base."""
        super().__init__(datos)

    def calcular_estadisticas(self):
        """Extiende el método para incluir datos adicionales."""
        estadisticas = super().calcular_estadisticas()
        estadisticas.loc['Varianza'] = self.df.var()
        estadisticas.loc['Mediana'] = self.df.median()
        return estadisticas
#datos

datos = [15, 20, 15, 18, 22, 13, 13, 16, 15, 19, 18, 15, 6, 20, 16, 15, 18, 16, 14, 13]

# Crear instancia de la clase
analisis = EstadisticaDescriptiva(datos)

# Calcular estadísticas descriptivas mejoradas
estadisticas = analisis.calcular_estadisticas()
print(estadisticas)

# Graficar histograma y diagrama de dispersión
analisis.graficar_histograma()
analisis.graficar_diagrama_dispersion()




  

          

