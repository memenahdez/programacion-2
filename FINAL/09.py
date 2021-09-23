#09

#pide la cantidad que quieres saber de dinero 
n = float(input("¿Qué cantidad desea insertar? "))
#Billetes de 500
a = 0
#Billetes de 200
b = 0
#Billetes de 100
c = 0
#Billetes de 50
d = 0
#Billetes de 20
e = 0

#Crea condicionales donde si la cantidad es dividida y mayor a 0 entonces el billete sera igual a la cantidad divida entre valor del billete

if n//500 > 0:
    a = n // 500
    n = n - (a*500)
if n//200 > 0:
    b = n // 200
    n = n - (b*200)
if n//100 > 0:
    c = n // 100
    n = n - (c*100)
if n//50 > 0:
    d = n // 50
    n = n - (d*50)
if n//20 > 0:
    e = n // 20
    n = n - (e*20)

print("Esta cantidad contiene:",a,"Billetes de 500,",b,"Billetes de 200,",c,"Billetes de 100,",d,"Billetes de 50,",e,"Billetes de 20,")
