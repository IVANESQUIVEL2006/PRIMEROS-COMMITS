def palabras_alrevez(frase):
    palabras = frase.split()  # Dividir la frase en palabras
    # es aqui donde se hace la reversa de cada palabra  inviviritendo la cadena 
    palabras_revertidas = [palabra[::-1] for palabra in palabras]  
    # el join es un metodo que comnbina una lista de cadenas en una sola cadena
    # las comillas son separadores con espacios 
    return ' '.join(palabras_revertidas)  # Unir las palabras invertidas

# es aqui donde empezamos a ejecutar el codigo
entrada = "soy ivan y mando saudos desde la unipoli"
salida = palabras_alrevez(entrada)
print(salida)  
