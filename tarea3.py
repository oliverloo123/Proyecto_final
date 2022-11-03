
op = "S"
cp = 0 
ci = 0


#pARa PONER MAYUSCULA
while op.upper()!='N': 

    numero = int(input("Ingrese un numero:"))

    if numero % 2 == 0:
       cp += 1 
    else:
       ci += 1

    op = input("Para terminar con la funcion precionar[N]: ")

print("Numeros de PARES: ", cp)
print("Numeros de IMPARES: ", ci)
