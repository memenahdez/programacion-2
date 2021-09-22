#02
#se le pide al usuario que escriba un numero minimo y máximo, en
#ciertos rangos dentro de uno general como el 1 al 10 debido a que
# a si  siempre habrá un numero mayor y menor.
minimo = int(input("Escribe un numero mínimo del 1 al 5"))

maximo =int (input("Escribe un numero máximo del 6 al 10"))

#la lista de numeros que pueden salir
numeros = [1,2,3,4,5,6,7,8,9,10]

#El rango esta definido para que muestre solo los mayores e iguales al minimo
#y menores o iguales al maximo.
for rango in numeros:
    if rango >= minimo and rango <= maximo:
        print (rango)

