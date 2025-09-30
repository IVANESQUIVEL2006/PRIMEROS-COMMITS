import re

def verificar_direccion_ipv4(ip):
    # Patrón para una dirección IPv4 válida
    patron = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not patron.match(ip):
        return False

    # Verificar que cada octeto esté en el rango de 0 a 255
    octetos = ip.split('.')
    for octeto in octetos:
        if int(octeto) < 0 or int(octeto) > 255:
            return False
    return True

def categoria_direccion_ipv4(ip):
    primer_octeto = int(ip.split('.')[0])
    if 1 <= primer_octeto <= 126:
        return "Clase A"
    elif 128 <= primer_octeto <= 191:
        return "Clase B"
    elif 192 <= primer_octeto <= 223:
        return "Clase C"
    elif 224 <= primer_octeto <= 239:
        return "Clase D (Multicast)"
    elif 240 <= primer_octeto <= 255:
        return "Clase E (Experimental)"
    else:
        return "No especificada"

def menu():
    print("Menú:")
    print("1. Verificar dirección IPv4")
    print("2. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            ip = input("Ingresa la dirección IPv4: ")
            if verificar_direccion_ipv4(ip):
                categoria = categoria_direccion_ipv4(ip)
                print(f"La dirección IPv4 es válida y pertenece a la {categoria}.")
            else:
                print("Error: La dirección IPv4 ingresada no es válida.")
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
