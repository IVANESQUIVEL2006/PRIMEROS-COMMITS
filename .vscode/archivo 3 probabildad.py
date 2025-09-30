import numpy as np
import pandas as pd

datos = [2, 4, 9, 7, 4, 5, 6, 5, 7, 7, 5, 5, 2, 10, 5, 6, 5, 4, 5, 8, 8, 4, 0, 8, 4, 8, 6, 6, 3, 6, 7, 6, 6, 7, 6, 7, 3, 5, 6, 9, 6, 1, 4, 6, 3, 5, 5, 6, 7]
df = pd.DataFrame(datos, columns=['Valor'])

estadisticas = df.describe()
print(estadisticas)