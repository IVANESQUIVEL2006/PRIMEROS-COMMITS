import pandas as pd
import matplotlib.pyplot as plt

# Datos de frecuencia calculados
total_aspirantes = 200
solo_matematicas = 40
solo_lenguaje = 20
aprobaron_ambas = 80
no_aprobaron_ninguna = 60

# Crear DataFrame para el análisis descriptivo
data = {
    'Grupo': ['Solo Matemáticas', 'Solo Lenguaje', 'Ambas Áreas', 'Ninguna'],
    'Frecuencia (Conteo)': [solo_matematicas, solo_lenguaje, aprobaron_ambas, no_aprobaron_ninguna]
}
df = pd.DataFrame(data)

# Calcular la Frecuencia Relativa (Probabilidad)
df['Frecuencia Relativa (Probabilidad)'] = df['Frecuencia (Conteo)'] / total_aspirantes

# --- 1. ESTADÍSTICA DESCRIPTIVA ---

# Encontrar la Moda (grupo con la mayor frecuencia)
moda_conteo = df['Frecuencia (Conteo)'].max()
grupo_modal = df[df['Frecuencia (Conteo)'] == moda_conteo]['Grupo'].iloc[0]

print("--- ESTADÍSTICA DESCRIPTIVA DEL EXAMEN ---")
print(f"Total de Aspirantes (N): {total_aspirantes}")
print(f"Moda (Grupo más frecuente): {grupo_modal} con {moda_conteo} aspirantes.")
print("\nTabla de Frecuencias y Frecuencias Relativas:")
print(df.to_string(index=False))

# --- 2. GRÁFICAS (VISUALIZACIÓN) ---

# A. Gráfica de Barras: Distribución de Frecuencia Absoluta (Conteo)
# [Se genera el archivo 'estadistica_descriptiva_bar_chart.png']

# B. Gráfica de Pastel: Distribución de Frecuencia Relativa (Probabilidad)
# [Se genera el archivo 'probabilidad_pie_chart_descriptiva.png']