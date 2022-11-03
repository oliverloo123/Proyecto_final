cadena = "hola mundo"
cadena_2 = "tu puedes conquistarla"
print(cadena,cadena_2)
print(len(cadena))

op = "S"

while op.upper()!='N':
    
    cad = input("Ingresar nombre: ")
    if len(cad)>=8:
       print(cad)

    else:
        print("Ingresar cadena mayor a 8 caracter")

    op = input("Para terminar con la funcion precionar[N]: ")
   
