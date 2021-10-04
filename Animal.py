class Animal:
    Patas = 4
    Bigotes = True
    Cola= 1
    Reino = "Animalia"
    Organismo = "Multicelular"

    def comer(self):
        boca = "Abrir"

    def dormir(self):
        boca = "Cerrar"

    def correr(self):
        boca = "Medio abierta"


    Perro = Animal()
    Gato = Animal()


Perro.correr()
Gato.dormir()
