def Login(nombre,password,intentos):
	intentos += 1
	if nombre == "usuario1" and password == "asdasd":
		return(True,intentos)
	else:
		return(False,intentos)

cuantasveces = 0

while True:
	usuario = input("Usuario:")
	clave = input("Password:")
	entrar,cuantasveces = Login(usuario,clave,cuantasveces)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces == 3: 
		break

if entrar:
	print("Bienvenidos al sistema")
else: 
	print("No has entrado en el sistema")

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
    elif opc=='6': 
        print('Adiós') 
        break  