def generar_direcciones_ip(base_ip, cantidad):
    base_octetos = base_ip.split(".")
    base_octetos = [int(octeto) for octeto in base_octetos]

    direcciones_ip = []
    for i in range(cantidad):
        nuevo_octeto = base_octetos[-1] + i
        nueva_ip = f"{base_octetos[0]}.{base_octetos[1]}.{base_octetos[2]}.{nuevo_octeto}"
        direcciones_ip.append(nueva_ip)
    
    return direcciones_ip

# Solicita al usuario la cantidad de direcciones a generar
cantidad = int(input("¿Cuántas direcciones IP deseas generar? "))
base_ip = "192.168.10.2" 

direcciones_generadas = generar_direcciones_ip(base_ip, cantidad)
for direccion in direcciones_generadas:
    print(direccion)
