#04
#Se crea una lista con los caracteres
caracteres = ["e","s","t","r","e","m","e","c","e","r"]
#Se crea un bucle for donde le pide que remplace todas las letra e por un 3
for contenido, letra in enumerate(caracteres):
    if letra == "e":
      caracteres[contenido] = 3

print(caracteres)
