#Inicializador Barcos

class Barco:
    flota = True
    tamaño = "a"
    compartimentos = "b"
    Pasajeros = "c"
    Peso = "d"
    tipo = "e"
    material ="f"

    def avanzar(self):
        print("el barco esta avanzando")

    def frenar(self):
        print("el barco esta frenando")

    def __init__(self,tamaño,pasajeros,tipo):
        self.tamaño = tamaño
        self.pasajeros = pasajeros
        self.tipo = tipo

velero = Barco("tamaño pequeño","9 pasajeros","Velero")
yate = Barco("tamaño mediano","25 pasajeros","yate")
catamaran = Barco("tamaño grande","80 pasajeros","catamarán")
canoa = Barco("tamaño pequeño","6 pasajeros","canoa")
lancha = Barco("tamaño mediano","20 pasajeros","lancha")

print("En un velero caben",velero.pasajeros)
print("En un yate caben",yate.pasajeros)
print("En un catamarán caben",catamaran.pasajeros)
print("En una canoa caben",canoa.pasajeros)
print("En una lancha caben",lancha.pasajeros)
