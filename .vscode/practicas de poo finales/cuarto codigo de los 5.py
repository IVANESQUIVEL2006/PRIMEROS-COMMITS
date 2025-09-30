def letra_no_repetida(cadena):
    # Esta línea es un bucle for que recorre un string (cadena de texto) letra por letra

    for caracter in cadena:
        # esta funcion busca el primer caracter no repetido 
        # el count cuenta cuantas veces aparece un caracter en una cadena
       # == 1: Si el carácter aparece exactamente 1 vez, significa que no está repetido.
        if cadena.count(caracter) == 1:
            # La función termina inmediatamente y devuelve el primer carácter que cumple la condición de no estar repetido.
            return caracter
        # Qué hace:
        #función devuelve None (que significa "nada" en Python) como señal de que no encontró ningún carácter no repetido.
    return None

# ais e como debeira de funcionar 
entrada = "aabbccdde"
resultado = letra_no_repetida(entrada)
print(resultado)  # como tendria que ejecutarse : 'c'