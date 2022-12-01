import random
def calcular(lista):
    return(max(lista),min(lista))

numero = []

for i in range(10):

    numero.append(random.randint(1,100))

Vmax,Vmin = calcular(numero)
print("El valor maximo es: ", Vmax)
print("El valor minimo es: ", Vmin)