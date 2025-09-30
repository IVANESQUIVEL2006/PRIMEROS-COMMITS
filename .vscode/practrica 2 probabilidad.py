import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def _init_(self,nombre):
    self.nombre=nombre

# Datos
datos = [3, 3, 4, 3, 4, 3, 1, 3, 4, 3, 3, 3, 2, 1, 3, 3, 3, 2, 3, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 3, 2, 1, 1, 1, 2, 2, 4, 1]

# Crear un DataFrame de pandas
df = pd.DataFrame(datos, columns=['Valores'])

# Calcular estadísticas descriptivas
estadisticas = df.describe()

# Imprimir la tabla de estadísticas
print(estadisticas)

# Graficar un histograma
plt.hist(df['Valores'], bins=4)
plt.title('Histograma de Valores')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt




