
#Programa: #validacion de direccion ip 
#descripcion:# este programa valida si una direccion por el usuario mac es valida
#Autor:JESUS IVAN ESQUIVEL RUIZ
#FECHA DE CREACION :31/01/2025
#VERSION : 1.0
#LENGUAJE:PYTHON
# Solicitar al usuario que ingrese una dirección MAC
# Solicitar al usuario que ingrese una dirección MAC
 
def verificar_categoria_mac(mac):
    categorias = {
        '00:1A:79': 'Cisco Systems, Inc',
        '00:25:96': 'Apple, Inc',
        '00:1B:63': 'Cisco Systems, Inc',
        # Agrega aquí más prefijos MAC y sus categorías
    }
    prefijo = mac[:8].upper()
    return categorias.get(prefijo, 'Error: Categoría no especificada')

def menu():
    print("Menú:")
    print("1. Verificar categoría de dirección MAC")
    print("2. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            mac = input("Ingresa la dirección MAC (formato XX:XX:XX:XX:XX:XX): ")
            categoria = verificar_categoria_mac(mac)
            print("Resultado:", categoria)
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()


