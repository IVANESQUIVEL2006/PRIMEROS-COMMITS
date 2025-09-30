import numpy as np
import pandas as pd

datos = [15, 20, 15, 18, 22, 13, 16, 19, 19, 18, 15, 20, 16, 15, 18, 14, 13]
df = pd.DataFrame(datos, columns=['Valor'])

estadisticas = df.describe()
print(estadisticas)
