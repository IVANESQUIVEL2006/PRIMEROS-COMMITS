import random

# 1. Crear lista, filtrar pares y elevar al cuadrado
numeros = [random.randint(1, 100) for _ in range(100)]
pares_cuadrados = []

for n in numeros:
    if n % 2 == 0:
        pares_cuadrados.append(n**2)

print("Pares al cuadrado:")
print(pares_cuadrados)

# 2. Crear lista, filtrar mayores a 50, elevar al cubo y sumar
numeros2 = [random.randint(1, 100) for _ in range(100)]
cubos_sumados = 0

for n in numeros2:
    if n > 50:
        cubos_sumados += n**3

print("\nSuma de cubos de números mayores a 50:")
print(cubos_sumados)

# 3. Aproximar pi con fórmula de Wallis sin funciones raras
producto = 1

for i in range(1, 100001):
    producto *= (4 * i * i) / (4 * i * i - 1)

pi_aprox = producto * 2

print("\nValor aproximado de pi (fórmula de Wallis):")
print(pi_aprox)
    
