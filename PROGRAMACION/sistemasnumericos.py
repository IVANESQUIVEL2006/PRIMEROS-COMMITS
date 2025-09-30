#nombre del programador:jesus Ivan Esquivel Ruiz
#nombre del programa: sistemas numericos 
#fecha de elaboracion: 14/03/2025
#ultima modificacion:14/03/2025
#programa ejecutado:PYTHON
#  




def binario_a_decimal(binario):
    """
    Convierte un número binario a decimal.
    
    Args:
        binario (str): Número en binario.

    Returns:
        int: Número en decimal.
    """
    return int(binario, 2)

def octal_a_decimal(octal):
    """
    Convierte un número octal a decimal.
    
    Args:
        octal (str): Número en octal.

    Returns:
        int: Número en decimal.
    """
    return int(octal, 8)

def hexadecimal_a_decimal(hexadecimal):
    """
    Convierte un número hexadecimal a decimal.
    
    Args:
        hexadecimal (str): Número en hexadecimal.

    Returns:
        int: Número en decimal.
    """
    return int(hexadecimal, 16)

def decimal_a_binario(decimal):
    """
    Convierte un número decimal a binario.
    
    Args:
        decimal (int): Número en decimal.

    Returns:
        str: Número en binario.
    """
    return bin(decimal)[2:]

def decimal_a_octal(decimal):
    """
    Convierte un número decimal a octal.
    
    Args:
        decimal (int): Número en decimal.

    Returns:
        str: Número en octal.
    """
    return oct(decimal)[2:]

def decimal_a_hexadecimal(decimal):
    """
    Convierte un número decimal a hexadecimal.
    
    Args:
        decimal (int): Número en decimal.

    Returns:
        str: Número en hexadecimal.
    """
    return hex(decimal)[2:]

def main():
    """
    Función principal del programa.
    """
    print("\n💀 ¡Bienvenido al Conversor de Números! 🎉\n")
    print("🇲🇽 Conversiones entre sistemas numéricos binario, octal, decimal y hexadecimal.\n")

    try:
        numero = input("🔢 Ingresa el número: ")
        sistema_origen = int(input("\nSelecciona el sistema de origen:\n1. Binario\n2. Octal\n3. Decimal\n4. Hexadecimal\n👉 Opción: "))
        sistema_destino = int(input("\nSelecciona el sistema de destino:\n1. Binario\n2. Octal\n3. Decimal\n4. Hexadecimal\n👉 Opción: "))

        decimal = None

        if sistema_origen == 1:
            decimal = binario_a_decimal(numero)
        elif sistema_origen == 2:
            decimal = octal_a_decimal(numero)
        elif sistema_origen == 3:
            decimal = int(numero)
        elif sistema_origen == 4:
            decimal = hexadecimal_a_decimal(numero)
        else:
            print("🚫 Sistema de origen inválido.")
            return

        if sistema_destino == 1:
            resultado = decimal_a_binario(decimal)
        elif sistema_destino == 2:
            resultado = decimal_a_octal(decimal)
        elif sistema_destino == 3:
            resultado = decimal
        elif sistema_destino == 4:
            resultado = decimal_a_hexadecimal(decimal)
        else:
            print("🚫 Sistema de destino inválido.")
            return

        print(f"\n✅ Resultado: {resultado}")

    except ValueError as e:
        print(f"\n⚠️ Error: Entrada no válida. {e}")

    print("\n✨ ¡Gracias por usar el Conversor de Números! 🌵🎉")
    print("¡Hasta la próxima! 🇲🇽\n")

if __name__ == "__main__":
    main()
