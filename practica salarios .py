import pandas as pd

# Lista de datos
datos = [2, 4, 9, 7, 4, 5, 6, 5, 7, 7, 5, 5, 2, 10, 5, 6, 5, 4, 5, 8, 4, 0, 8, 8, 6, 3, 6, 7, 6, 6, 7, 6, 7, 3, 5, 6, 9, 6, 1, 4, 6, 3, 5, 5, 6, 7]

# Crear un DataFrame
df = pd.DataFrame(datos, columns=['Datos'])

# Generar la tabla de frecuencias
tabla_frecuencias = df['Datos'].value_counts().reset_index()
tabla_frecuencias.columns = ['Dato', 'Frecuencia']

# Guardar la tabla en un archivo de Excel
tabla_frecuencias.to_excel('tabla_frecuencias_datos.xlsx', index=False)

print("Tabla de frecuencias guardada en 'tabla_frecuencias_datos.xlsx'.")

