#Inicializador Autos

class Auto():
    pasajeros = "a"
    tipo = "b"
    volante = True
    marca = "c"
    motor = True


    def __init__(self,pasajeros,tipo,marca):
        self.pasajeros = pasajeros
        self.tipo = tipo
        self.marca = marca

camión = Auto("28 pasajeros","camión","Volvo")
auto_deportivo = Auto("2 pasajeros","deportivo","Ferrari")
autobus = Auto("120 pasajeros","autobus","ETN")
camioneta = Auto("7 pasajeros","camioneta","Toyota")
trailer = Auto("2 pasajeros","trailer","Internacional")


print("Este camión es marca",camión.marca)
print("Este auto deportivo es marca",auto_deportivo.marca)
print("Este autobus es marca",autobus.marca)
print("Esta camioneta es marca",camioneta.marca)
print("Este trailer es marca",trailer.marca)

    
    
