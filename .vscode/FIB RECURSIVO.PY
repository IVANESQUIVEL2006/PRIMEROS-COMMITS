# FIB RECURSIVO
def fibonacci(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        lista = fibonacci(n-1)
        return lista+[lista[n-2]+lista[n-3]]
    return lista
a=fibonacci(6)
print(a)

