class Auto:
    Llantas = 4
    Color = Azul
    Puertas = 5
    Volante = True
    Asientos = 5


    def encender(self):
        motor = "encendido"

    def apagar(self):
        motor ="apagado"

    def acelerar(self):
        motor = "acelerado"

Audi = Auto()
BMW = Auto()
Mazda = Auto()

Audi.apagar()
Mazda.encender()
BMW.acelerar()
