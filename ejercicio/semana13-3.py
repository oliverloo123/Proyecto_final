def temperatura(T1,T2):
    return(T1 + T2)/2

cantidad = int(input("¿Cuanta temperatura vas a calcular?: "))
for indice in range(cantidad):
    Tmax = float(input("Introduce temperatura minima: "))
    Tmin = float(input("Introduce temperatura maxima: "))
    print("Temperatura media: ", temperatura(Tmax,Tmin))