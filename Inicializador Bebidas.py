#Inicializador bebidas

class Bebida:
    liquido = True
    Gas = "g"
    Azucar = "z"
    Sabor = "s"
    Agua = "a"


    def beber(self):
        print("la bebida esta siendo bebida")
        
    def servir(self):
        print("la bebida esta siendo servida")

    def __init__(self,gas, sabor, azucar,agua):
        self.gas = gas
        self.sabor = sabor
        self.azucar = azucar
        self.agua = agua

agua_de_limón = Bebida("sin gas","sabor limón","0g de azúcar","75% de agua")
cocacola = Bebida("con gas","sabor refresco","9g de azúcar","50% de agua")
cafe = Bebida("sin gas","sabor café","2g de azúcar","25% de agua")
agua_pura = Bebida("sin gas","sabor agua","0g de azúcar","100% de agua")
agua_de_naranja = Bebida("sin gas","sabor naranja","3g de azúcar","70% de agua")
        
print("el agua de naranja tiene",agua_de_naranja.sabor)
print("el agua de limon tiene",agua_de_limón.sabor)
print("la cocacola tiene",cocacola.sabor)
print("el agua tiene",agua_pura.sabor)
print("el cafe tiene",cafe.sabor)
