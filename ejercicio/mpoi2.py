from math import sqrt

def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplicacion(x,y):
    return x*y
def division(x,y):
    if y != 0:
        return x/y
    return "No se puede dividir"
def potencia(x,y):
    return pow(x,y)



n1 = float(input("N1: "))
n2 = float(input("N2: "))

print("La suma es: ", (suma(n1,n2)))
print("La resta es: ", (resta(n1,n2)))
print("La multiplcaion es: ", (multiplicacion(n1,n2)))
print("La division es: ", (division(n1,n2)))
print("La division es: ", (potencia(n1,n2)))