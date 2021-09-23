#12
#se crea la lista de los 10 numeros
numeros = [1,2,3,4,5,6,7,8,9,10]
#se hace un apartado vacio donde se recibiran los pares
pares = []
#se hace una condición para que identifique los pares
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)
#Se manda a imprimir la suma con la función "sum"

print ("la suma de los numeros pares del 1 al 10 es", sum(pares))
