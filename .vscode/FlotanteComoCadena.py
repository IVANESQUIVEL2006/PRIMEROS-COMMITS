def operaciones_numero(cadena_flotante):
    try:
        # Convertir la cadena flotante a número flotante
        numero_flotante = float(cadena_flotante)
        
        # Convertir el número flotante a entero
        numero_entero = int(numero_flotante)
        
        # Realizar operaciones
        suma = numero_entero + 10
        multiplicacion = numero_entero * 5
           
        division = numero_entero / 2

        # Imprimir resultados
        print(f"Número entero: {numero_entero}")
        print(f"Suma (+10): {suma}")
        print(f"Multiplicación (*5): {multiplicacion}")
        print(f"División (/2): {division:.2f}")

    except ValueError:
        print("La cadena proporcionada no es un número flotante válido.")

# Ejemplo de uso
cadena_flotante = "123.45"
operaciones_numero(cadena_flotante)

