
print("ELIGE UNA OPCION")

print("[1]Circulo")
print("[2]Triangulo")

opcion = int(input("Ingrese la opcion: "))

if opcion == 1:
     radio = float(input("Ingrese el valor de la radio: " ))
     PI = 3.14
     area = PI * radio * radio
     print(" El area es  :",area)

elif opcion == 2:
     b=int(input("Ingrese la base: "))
     h=int(input("Ingrese la altura: "))
     area=b*h/2
     print("El area es : ",area)