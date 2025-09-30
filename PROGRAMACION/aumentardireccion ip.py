def generar_direcciones_ip(base_ip, cantidad):
    # Dividir la IP base en sus octetos
    octetos = base_ip.split('.')
    
    # Convertir los octetos a enteros
    octetos = [int(octeto) for octeto in octetos]
    
    direcciones_ip = []
    
    for i in range(cantidad):
        # Agregar la IP generada a la lista
        direcciones_ip.append(f"{octetos[0]}.{octetos[1]}.{octetos[2]}.{octetos[3] + i}")
        
        # Verificar si se ha alcanzado el límite del último octeto
        if (octetos[3] + i) >= 255:
            # Reiniciar el último octeto y aumentar el penúltimo octeto
            octetos[3] = (octetos[3] + i) % 255
            octetos[2] += 1
            i = -1  # Restablecer el índice para continuar desde la nueva base IP
    
    return direcciones_ip

def main():
    # Preguntar cuántas direcciones IP se desean generar
    cantidad = int(input("¿Cuántas direcciones IP deseas generar? "))

    # Solicitar la dirección IP inicial
    base_ip = input("Ingresa la dirección IP inicial (formato: xxx.xxx.xxx.xxx): ")

    # Generar las direcciones IP
    ips_generadas = generar_direcciones_ip(base_ip, cantidad)

    # Mostrar las direcciones IP generadas
    for ip in ips_generadas:
        print(ip)

if __name__ == "__main__":
    main()
