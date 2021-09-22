#08

#Se realiza una lista con 20 nombres comunes
nombres = ["ana","sofia","ale","juan","luis", "angel","jesús","ximena","sabrina", "josé","damian","berenice", "johana", "eduardo","javiera","america","brian","diego","mar","angela"]
#Se manda a imprimir la lista de nombres para que el usuario los visualice
print ("la lista de nombres actual es:",nombres)
#Se realiza otra lista pero ahora con los nombres que se eliminaran de la principal
eliminados = {"ana","sofia","juan","luis","johana", "eduardo"}
#Se crea una nueva lista donde haga una condición en la primera lista donde los nombres que estan en la segunda lista estan en la principal son eliminados
lista_nueva = [lista for lista in nombres if lista not in eliminados]
#Se manda a imprimir la lista nueva
print("Lista con elementos removidos", lista_nueva)
