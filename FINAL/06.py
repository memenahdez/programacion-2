#06
numero = int(input("Dame un número para saber si es primo: "))
#los numero primos tienen que ser divisibles entre si mismos y entre 1, al igual que tienen que ser mayor que 1.
i = 2
while numero % i > 0:
    i = i + 1
if  i == numero:
    print("Es primo")
else:
    print("NO es primo")


