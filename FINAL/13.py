#13 Año bisiesto

año = int(input("Ponga un año para saber si es bisiesto"))

#Se pone una condición ya que cada 4 año es bisiesto, pero también tiene que ser multiplo de 400

if año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    print ("es divisible entre 4 pero no entre 4200 por lo que NO es bisiesto")

elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("El año seleccionado es bisiesto")
    
else:
    print("El año seleccionado NO es bisiesto")
