cad = input("cadena: ")
caracter = input("caracter: ")
for i in range(0,9):
    cad = cad.replace(str(i),caracter)
print(cad)