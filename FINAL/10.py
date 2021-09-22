#10- Crea un programa que te pida la hora, y te en ese mismo momento  la hora en España, Japón, Australia y China.
from datetime import datetime
import pytz
UTC = pytz.utc
ACST = pytz.timezone ("Australia central")
print("la hora de australia es: ", datetime.now(ACST))





ahora = datetime.now()
hora = input("¿Cúal es la hora en tu zona?")

def pedir_horas():
    print ("La hora en España, Japón, Australia y China son las siguientes")
    print (ahora.hour, "horas")




pedir_horas()
