mensaje = "abcd"
clave = 5
alfabeto = "abcdefghijklmnopqrstuvwxyz"
resultado = ""


for letra in mensaje:
     # el index busca un elemento dentro de una cadena o lista y te dice en qué posición está
    posicion = alfabeto.index(letra)
    # Esta línea toma la posición de la letra, le suma la clave, y si se pasa de la “z” empieza otra vez desde la “a”.
    nueva_posicion = (posicion + clave) % 26

    #En resumen: esa línea mete la letra cifrada al “cajón” (resultado) que guardará todo el mensaje final.
    #el +- agrega y asigna
    resultado += alfabeto[nueva_posicion]

print(resultado)
