palabra1="roma"
palabra2="amor"

#  el sorted ordena los elementos de una lista de forma ascendente o decendente 
# verifica que dos litas tengaan los mismos elementos
# vueve a ordenar los datos
p1 = sorted(palabra1)
p2 = sorted(palabra2)
# aqui es donde se evalua  s1 y s2 tienen el mismo valor,guardando el resultado de la comparacion 
iguales = p1 == p2
print(iguales)
