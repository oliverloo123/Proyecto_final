def menuart(): 
    print() 
    print('1) Ingresar artículo') 
    print('2) Consultar artículo') 
    print('3) Comprar') 
    print('4) Vender') 
    print('5) Eliminar artículo') 
    print('6) login') 
    print("7).salir")
     
def ingresar(registros): 
    cod=int(input('Ingrese código: ')) 
    cant=int(input('Ingrese cantidad: ')) 
    pre=float(input('Ingrese precio: ')) 
    nom=input('Ingrese nombre: ') 
    reg=[cod,cant,pre,nom] 
    registros=registros+[reg] 
    return registros 
 
def consultar(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        print('Cantidad: ',registros[p][1]) 
        print('Precio: ',registros[p][2]) 
        print('Nombre: ',registros[p][3]) 
         
def comprar(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        k=int(input('Ingrese la cantidad comprada: ')) 
        registros[p][1]=registros[p][1]+k 
    return registros 

def vender(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1;  
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        k=int(input('Ingrese la cantidad vendida: ')) 
        registros[p][1]=registros[p][1]-k 
    return registros 
 
def eliminar(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        del registros[p] 
    return registros 

def login():
    user_ = "admin"
    pwd_ = "pepe grillo"
    print("===Bienvenido===")
    print("Ingrese sus datos: ")
    print("Usuario: ")
    user = input()
    print("Contraseña:")
    pwd = input()
    if user==user_ and pwd==pwd_:
        print("Bienvenido al programa: ")
    
  
registros=[] 
while True: 
    menuart() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        registros=ingresar(registros) 
    elif opc=='2': 
        consultar(registros) 
    elif opc=='3': 
        registros=comprar(registros)      
    elif opc=='4': 
        registros=vender(registros)             
    elif opc=='5': 
        registros=eliminar(registros) 
    elif opc == "6":
        registros = login(registros)            
    elif opc=='7': 
        print('Adiós') 
        break  
     