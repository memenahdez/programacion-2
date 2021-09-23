#10- Crea un programa que te pida la hora, y te de en ese mismo momento  la hora en España, Japón, Australia y China.
#importa la fecha y el tiempo transcurrido entre dos fechas
from datetime import datetime
from datetime import timedelta
#pide la hora actual y después se imprime la hora en los distintos paises dependiento a cuantas horas más tienen a comparación de méxico
ahora = datetime.now()
hora = input("¿Cúal es la hora en tu zona?")
España = ahora + timedelta(hours=7)
Japón = ahora + timedelta(hours=14)
Australia = ahora + timedelta(hours=15)
China = ahora + timedelta(hours=13)
print ("en España son", España, "horas")
print ("en Japón son", Japón, "horas")
print ("en Australia son", Australia, "horas")
print ("en China son", China, "horas")
