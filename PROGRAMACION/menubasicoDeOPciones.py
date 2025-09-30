#jesus Ivan Esquivel Ruiz
#materia:programacion
#fecha:05/02/2025
#descripcion del programa:este programa genera un menu basico de opciones que el usuario puede generar y controlar como:saludar,mostrar un numero,decir adios y salir

def mostrar_menu():
    print("\nMenu de Opciones:")
    print("1. Saludar")
    print("2. Mostrar un número")
    print("3. Decir adiós")
    print("4. Salir")

def saludar():
    print("¡Hola! ¿Cómo estás?")

def mostrar_numero():
    numero = 42
    print(f"El número es: {numero}")

def decir_adios():
    print("¡Adiós! Que tengas un buen día.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            saludar()
        elif opcion == "2":
            mostrar_numero()
        elif opcion == "3":
            decir_adios()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
