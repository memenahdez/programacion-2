#Inicializador Felinos

class Felino():
    peso = "a"
    fuerza ="b"
    bigotes = True
    cola = 1
    patas = 4
    habitat ="c"


    def comer(self):
        print("El felino esta comiendo")

    def dormir(self):
        print("El felino esta durmiendo")

    def __init__(self,peso,fuerza,habitat):
        self.peso = peso
        self.fuerza = fuerza
        self.habitat = habitat
    

gato = Felino("pesa 4.5 kg","poca fuerza","hogares")
tigre = Felino("pesa 4.5 kg","gran fuerza","selvas, sabanas y manglares")
león = Felino("pesa 190 kg","la mayor fuerza","sabanas")
puma = Felino("pesa 100 kg","gran fuerza","bosques")
leopardo = Felino("pesa 31 kg","gran fuerza","sabanas, montañas y selvas")


print("Los gatos viven en",gato.habitat)
print("Los tigres viven en",tigre.habitat)
print("Los leones viven en",león.habitat)
print("Los pumas viven en",puma.habitat)
print("Los leopardos vive en",leopardo.habitat)

