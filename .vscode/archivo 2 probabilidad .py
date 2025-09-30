import numpy as np
import pandas as pd

datos = [3, 4, 3, 1, 3, 1, 4, 3, 2, 3, 1, 3, 3, 2, 2, 3, 3, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 1, 1, 2, 2, 1, 4]
df = pd.DataFrame(datos, columns=['Valor'])

estadisticas = df.describe()
print(estadisticas)