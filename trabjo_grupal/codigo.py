a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrse el segundo numero: "))

def sema_a():
    s = 0
    for n in range(1,a):
        if a%n == 0:
            s=s+n
    return s




