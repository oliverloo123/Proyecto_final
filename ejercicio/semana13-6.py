import math
def calcularAreaPerimetro(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area,perimetro

radio = float(input("Introduce el radio: "))
area,perimetro = calcularAreaPerimetro(radio)
print("Area: ", area)
print("Perimetro: ", perimetro)
