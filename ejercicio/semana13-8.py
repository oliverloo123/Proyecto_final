def calculo_factorial(num):
    if num == 1:
        return 1
    else:
        return num * calculo_factorial(num-1)

numero1 = int(input("Numero: "))
print("El factorial es: ", calculo_factorial(numero1))