def menuart(): 
    print() 
    print('1) Grande') 
    print('2) Pequeña') 
    print('3) Mediana') 
    print('4) Salir')

def grande():
    print("Usted eligio la pizza tamaño grande")
    precio = int(input("Ingrese el precio de la pizza: "))

    print("//## Ingrediente Adicional ##//")
    print("1). Si ")
    print("2). No ")
    op = input("Ingrese la opcion si quiere ingrediente adicional: ")

    if op == "Si":
        adi = int(input("Ingrese cuando inrediet quieres"))
        precio_total = precio + 1.5
        print("Su pago total es: ", precio_total)
    else:
        print("Su pizza tendra con los ingredientes basicos")







while True: 
    menuart() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        grande() 
    elif opc=='2': 
        pequeña() 
    elif opc=='3': 
        mediana()                 
    elif opc=='4': 
        print('Adiós') 
        break  

