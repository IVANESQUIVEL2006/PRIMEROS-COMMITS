def validar_octeto(octeto):
    try:
        valor = int(octeto)
        return 0 <= valor <= 255
    except ValueError:
        return False

def validar_direccion_ip(direccion_ip):
    octetos = direccion_ip.split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        if not validar_octeto(octeto):
            return False
    return True

# Prueba la función con una dirección IP
direccion_ip = "192.168.0.1"
if validar_direccion_ip(direccion_ip):
    print(f"La dirección IP {direccion_ip} es válida.")
else:
    print(f"La dirección IP {direccion_ip} no es válida.")
