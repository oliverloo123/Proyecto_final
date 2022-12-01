
op = "S"
contador = 0 
suma  = 0

while op.upper()!='N':
    contador += 1 
    numero = int(input("Ingrese un numero:"))
    suma += numero
    op = input("Para terminar con la funcion precionar[N]: ")

print("El promedio es ",(suma / contador))