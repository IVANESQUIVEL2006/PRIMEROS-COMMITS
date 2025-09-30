input("ingresa una direccion ip")

octetos=direccion_ip.split(".")
es_valida = True

if len(octetos)  !=4:
    es_valida= False
else:
 for octeto in octetos
if not octeto .isdigit() or not <(0<= int(octeto)>=255):
   es_valida = False
   break
if es_valida
print()

print len (octetos)
for octeto in octetos:
if not octeto.isdigitC)
print(" no es un valor valido")

else
