def multiplo(N1,N2):
    if N1 % N2 == 0:
        return True
    else:
        return False

Nu1 = int(input("Numero 1: "))
Nu2 = int(input("Numero 2: "))

if multiplo(Nu1,Nu2):
    print(Nu1, "es multiplo de ", Nu2)
else:
    print(Nu1, "no es multiplo de ", Nu2)