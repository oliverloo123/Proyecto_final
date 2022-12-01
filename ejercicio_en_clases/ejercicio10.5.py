cad = input("numero: ")
car = input("caracter: ")
cont = 0
cad2 = ""
for c in cad:
    if cont != 0 and cont%3 == 0:
        cad2 = cad2 + car
    cad2 = cad2 + c
    cont = cont + 1
print(cad2)