def calculadora():
    # Emojis para decorar
    SUMA = "➕"
    RESTA = "➖"
    MULTI = "✖️"
    DIV = "➗"
    IGUAL = "➡️"
    ERROR = "❌"
    BIENVENIDA = "👋"
    DESPEDIDA = "👾"

    print(f"{BIENVENIDA} Bienvenido a la Calculadora Profesional v1.0")
    print("==========================================")

    try:
        # Solicitar números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Realizar operaciones
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        
        # Verificar división por cero
        if num2 == 0:
            division = f"{ERROR} No se puede dividir por cero"
        else:
            division = num1 / num2

        # Mostrar resultados con emojis y formato
        print("\nResultados:")
        print("===========")
        print(f"{SUMA} Suma: {num1} + {num2} {IGUAL} {suma:.2f}")
        print(f"{RESTA} Resta: {num1} - {num2} {IGUAL} {resta:.2f}")
        print(f"{MULTI} Multiplicación: {num1} × {num2} {IGUAL} {multiplicacion:.2f}")
        print(f"{DIV} División: {num1} ÷ {num2} {IGUAL} {division}")

    except ValueError:
        print(f"{ERROR} Por favor, ingrese solo números válidos")
    except Exception as e:
        print(f"{ERROR} Ha ocurrido un error: {e}")

    print(f"\n{DESPEDIDA} Gracias por usar la calculadora!")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()