def analizar_direccion_ipv4(direccion):
    """
    Analiza una dirección IPv4 y determina su clase y tipo.
    """
    try:
        octetos = direccion.split(".")
        if len(octetos) != 4:
            raise ValueError("Formato de dirección IPv4 inválido")

        primer_octeto = int(octetos[0])
        if not all(0 <= int(octeto) <= 255 for octeto in octetos):
            raise ValueError("Octetos fuera de rango")

        if primer_octeto == 127:
            return "Loopback"
        elif primer_octeto == 0 and all(int(octeto) == 0 for octeto in octetos):
            return "Red no especificada"
        elif 1 <= primer_octeto <= 126:
            return "Clase A"
        elif 128 <= primer_octeto <= 191:
            return "Clase B"
        elif 192 <= primer_octeto <= 223:
            return "Clase C"
        elif 224 <= primer_octeto <= 239:
            return "Clase D (Multicast)"
        elif 240 <= primer_octeto <= 255:
            return "Clase E (Reservado)"
        else:
            return "Desconocida"

    except ValueError as e:
        return str(e)


if __name__ == "__main__":
    while True:
        direccion = input("Ingrese una dirección IPv4 (o 'salir' para terminar): ")
        if direccion.lower() == "salir":
            break

        resultado = analizar_direccion_ipv4(direccion)
        print(f"La dirección {direccion} pertenece a: {resultado}\n")1
        





