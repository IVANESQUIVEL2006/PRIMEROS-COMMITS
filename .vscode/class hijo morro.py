#FIBONACCI FOR 
n=6
if n < 0:
    pass
elif n==1:
    print(0)
else:
    lista=[0 ,1]
    for i in range(2,n):
        lista.append(lista[i-1]+lista[i-2])
        print(lista)



