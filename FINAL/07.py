#07
#la función te pide que insertes una de las palabras que te pone

def contar_palabras():
    print("Escoge una palabra de las siguientes:", "uno", "dos","tres")
#se crea una lista con los numeros repetidos diferentes veces
    lista = ["uno", "dos", "tres","uno", "dos", "tres","dos", "tres","dos", "tres", "tres"]
    numero = input("Escoge tu palabra")
#se aplica una condicional donde dice que si la palabra es igual al numer0 1,2 o 3
#se imprimira un contados de cuantas veces la palabra aparece en la lista
    if numero == "uno":
        print ("la palabra", numero, "se repite", lista.count("uno"), "veces")
    elif numero =="dos":
        print ("la palabra", numero, "se repite", lista.count("dos"), "veces")
    else:
        print ("la palabra", numero, "se repite", lista.count("tres"), "veces")
#se llama la función
contar_palabras()
