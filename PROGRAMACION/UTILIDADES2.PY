# Funciones para las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

# Menú de utilidades
def menu():
    print("🧮 Calculadora de Operaciones Básicas 🧮")
    print("1️⃣. Sumar")
    print("2️⃣. Restar")
    print("3️⃣. Multiplicar")
    print("4️⃣. Dividir")
    print("5️⃣. Salir")
    print("")

    while True:
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {sumar(a, b)}")
        elif opcion == '2':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {restar(a, b)}")
        elif opcion == '3':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == '4':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {dividir(a, b)}")
        elif opcion == '5':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida, por favor seleccione una opción del 1 al 5.")

def obtener_numeros():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingrese números válidos.")
        return None, None

# Ejecutar el menú
menu()

