N1 = int(input("Ingrese el primer valor: "))
N2 = int(input("Ingrese el segundo valor: "))
N3 = int(input("Ingrese el tercer valor: "))

if N1 > N2 and N1 > N3:
    print("El primer valor",N1,"es mayor a los tres valores")
elif N2 > N3 and N2 > N1:
    print("El segundo valor",N2,"es mayor a los tres valores")
else:
    print("El tercer valor",N3,"es mayor a los tres valores")

N1 == N2 == N3
print(N1,",",N2,"y",N3,"son igules")