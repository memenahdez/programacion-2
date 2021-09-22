#Crear una Programa que te pida una cantidad de días y te diga cuantos segundos, días y minutos son.

#El programa pedira que se le diga la cantidad de días que quiere convertir a minutos y segundos
dia = int(input("selecciona una cantidad de días para convertirlo en días, minutos y segundos"))
#Se inserta una variable donde hace una multiplicacion de cuantos dias hay en día multiplicado por el numero de dias deseados
dias = dia * 1
#Se inserta una variable donde hace una multiplicacion de cuantos minutos hay en día multiplicado por el numero de dias deseados
minutos = dia * 1440
#Se inserta una variable donde hace una multiplicacion de cuantos segundos hay en día multiplicado por el numero de dias deseados
segundos =  dia * 86400
#Se manda a impirmir el resultado de esas multiplicaciones
print ("hay", dias,"dias","con",minutos,"minutos", "y", segundos, "segundos", "en la cantidad que seleccionaste")

