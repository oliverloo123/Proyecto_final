op = 1
texto = ""
cont = 0 
cv = 0

while op != 11:
    print("======MENÚ======")
    print("[1]. Ingresar Cadena.")
    print("[2]. Buscar cadena.")
    print("[3]. Reemplazar cadena.")
    print("[4]. Captalizar el primera caracter de la cadena.")
    print("[5]. Convertir en minusculas.")
    print("[6]. Convertir en mayusculas.")
    print("[7]. Eliminar los espacios en blanco de la cadena.")
    print("[8]. Alinear a la izquierda.")
    print("[9]. Alinear a la derecha.")
    print("[10]. Alinear al centro.")
    print("[11]. Salir.")
    op = int(input("Ingrese una opción del [1-11]: "))

    if op == 1:
        texto = input("Ingrese frase: ")
    if op == 2:
        cad = input("Ingresar palabra a bsucar: ")
        ubi = texto.find(cad)
        if ubi>=0:
            print("Palabra encontrada y su posición: ", ubi)
        else:
            print("Palabra no existe en la frase...")
    if op == 3:
        cand_ant = input("Ingrese la palabra a buscar: ")
        cad_nu = input("Ingrese la palabra a reemplazar: ")
        texto.replace(cand_ant,cad_nu)
        print(texto)
    if op == 4:
        print(texto.capitalize())
    if op == 5:
        print(texto.lower())
    if op == 6:
        print(texto.upper())
    if op == 7:
        print(texto.strip())
    if op == 8:
        print('{:^100}'.format(texto))
    if op == 9:
        print('{:>100}'.format(texto))
    if op == 10:
        print('{:100}'.format(texto))






