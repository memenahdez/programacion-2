#Inicializador Celulares

class Celular():
    tamaño = "a"
    bateria = 1
    pantalla = 1
    color = "b"
    marca = "c"
    cargador = True

    def __init__(self,tamaño,color,marca):
        self.tamaño = tamaño
        self.color = color
        self.marca = marca

iphone_XR = Celular("su pantalla mide 6.06 pulgadas","negro, gris, rojo","Apple")
Samsung_Galaxy_S20 = Celular("su pantalla mide 6,2 pulgadas","negro y azul","Samsung")
Motorola_Moto_E6 = Celular("su pantalla mide 6,1 pulgadas","negro","Motorola")
Huawei_P40 = Celular("su pantalla mide 6,1 pulgadas","negro","Huawei")
iphone_13_mini = Celular("su pantalla mide 5,4 pulgadas","negro","Apple")


print("El iphone XR es",iphone_XR.marca)
print("El samsung galaxy s20 es",Samsung_Galaxy_S20.marca)
print("El motorola moto e6 es",Motorola_Moto_E6.marca)
print("El huawei p40 es",Huawei_P40.marca)
print("El iphone 13 mini es",iphone_13_mini.marca)



    
