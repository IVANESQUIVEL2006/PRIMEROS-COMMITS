import pandas as pd

# Lista de datos
datos = [
    84, 85, 85, 86, 86, 86, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 88,
    88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 
    89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 90, 90, 90, 90, 
    90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 
    91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 
    93, 93, 94, 95
]

# Crear un DataFrame
df = pd.DataFrame(datos, columns=['Datos'])

# Generar la tabla de estadística descriptiva
tabla_estadistica = df.describe()

# Mostrar la tabla
print(tabla_estadistica)


