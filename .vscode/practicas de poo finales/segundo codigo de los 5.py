def rotacion_de_listas(lista1, lista2):
    # debemos de verificar si la longitud de las listas son iguales

# esta linea de codigo compara si los elementos son diferentes
    if len(lista1) != len(lista2):
        return False
    
    # unir lista1 consigo misma
    lista_cambiada_de_forma_ordenada = lista1 + lista1
    
    # Verificar si lista2 está en la cadena de lista1
    # la  siguiente linea de codigo la hice parra reorrer los indices de la lista uno por uno
    # En este caso, len(lista1) devuelve la cantidad de elementos que contiene la lista llamada lista1.
    for i in range(len(lista1)):
       # el len lo que hace es 
       
        # aqui es donde combinamos todas las rotaciones posibles,extrayendo cada rotacion y comparando si esa rotacion concide con la lista2
        
   #     # en la lisa 1 lem em devolveria 
        if lista_cambiada_de_forma_ordenada[i:i + len(lista1)] == lista2:
            # las siguientes son las respuestas definitivas de la funcion  si la rotacion es correcta o no
            return True
        # el len  es la longitud de la lis
    
    return False

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 1, 2]
print(rotacion_de_listas(lista1, lista2))  # Output: True




