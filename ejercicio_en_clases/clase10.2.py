op = 1
texto = ""
cont = 0 
cv = 0

while op != 5:
    print("======MENÚ======")
    print("[1]. Ingresar Cadena.")
    print("[2]. # de espacio en blnaco.")
    print("[3]. # de Vocales.")
    print("[4]. Dimencion de la cadena.")
    print("[5]. Salir.")

    op = int(input("Ingrese una opción del [1-5]: "))

    if op == 1:
        texto = input("Ingrese frase: ")

    if op == 2:
        for cad in range(0,len(texto)):
            if texto[cad] == " ":
                cont+=1    
        print("# de espacio en blnaco: ", cont)

    if op == 3:
        for cad in range(0, len(texto)):
           if texto[cad] == "a" or texto[cad] == "e" or texto[cad] == "i" or texto[cad] == "o" or texto[cad] == "u":
               cv+=1
        print("# de vocales: ", cv)

    if op == 4:
       print("Longitud de la cadena: ",len(texto))