from math import sqrt 

catA = int(input("Ingrese el numero del cateto ayacente: "))
catB = int(input("Ingrese el numero del cateto opuesto: "))

formula = sqrt(pow(catA,2) + pow(catB,2))

print("Su hipotenusa es: ", formula)