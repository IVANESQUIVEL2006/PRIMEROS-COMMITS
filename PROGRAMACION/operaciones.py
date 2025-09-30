# Jesus Ivan Esquivel Ruiz
# programa: python
# version del programa: 3.10.11
# descripcion del programa: este codigo genera suma de dos o mas numeros, resta de dos o mas numeros, multiplicacion de dos numeros y division de dos o mas numeros y si alguno no corresponde a esto mandara un error asi como si estos numeros son igualados a 0
# materia: programacion
# fecha de creacion del programa: 27/02/2025
# ultima modificacion del programa: 27/02/2025
import operaciones

def obtener_numeros():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingrese números válidos.")
        return None, None

def obtener_varios_numeros():
    try:
        numeros = input("Ingrese los números separados por comas: ")
        lista_numeros = [float(num) for num in numeros.split(',')]
        return lista_numeros
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingrese números válidos.")
        return None

def menu():
    print(" Calculadora de Operaciones Básicas ")
    print(" ¡Bienvenido! ¿En qué te puedo ayudar hoy?")
    print("1️⃣. Sumar dos números")
    print("2️⃣. Sumar varios números")
    print("3️⃣. Restar dos números")
    print("4️⃣. Multiplicar dos números")
    print("5️⃣. Multiplicar varios números")
    print("6️⃣. Dividir dos números")
    print("7️⃣. Salir")
    print("")

    while True:
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {operaciones.sumar(a, b)}")
        elif opcion == '2':
            numeros = obtener_varios_numeros()
            if numeros is not None:
                print(f"Resultado: {operaciones.sumar_varios(*numeros)}")
        elif opcion == '3':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {operaciones.restar(a, b)}")
        elif opcion == '4':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {operaciones.multiplicar(a, b)}")
        elif opcion == '5':
            numeros = obtener_varios_numeros()
            if numeros is not None:
                print(f"Resultado: {operaciones.multiplicar_varios(*numeros)}")
        elif opcion == '6':
            a, b = obtener_numeros()
            if a is not None and b is not None:
                print(f"Resultado: {operaciones.dividir(a, b)}")
        elif opcion == '7':
            print(" ¡Hasta luego! ¡Que tengas un buen día!")
            break
        else:
            print("⚠️ Opción no válida, por favor seleccione una opción del 1 al 7.")

# Ejecutar el menú
menu()

        


