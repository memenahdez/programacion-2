#05
# le pide al usuario que escoga entre esos numeros para que se haga la suma de la lista que le corresponde
numero = int(input("Escoga un numero del 1 al 5 y se sumara en su respectiva lista"))
seleccionado = numero
# se hacen las condicionales dependiendo del numero que escogió el usuario
if seleccionado == 1:
    lista = [10]
    print(sum(lista))

if seleccionado == 2:
    lista2 = [2,4]
    print(sum(lista2))

if seleccionado == 3:
    lista3 = [1,3,6]
    print(sum(lista3))

if seleccionado == 4:
    lista4 = [3,2,6,10]
    print(sum(lista4))

if seleccionado == 5:
    lista5 = [3,4,5,9,1]
    print(sum(lista5))



     
     
