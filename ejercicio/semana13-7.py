def login(nombre,contraseña, intentos):
    intentos += 1
    if nombre == "usuario1" and contraseña == "login":
        return(True,intentos)
    else:
        return(False,intentos)

cuantas_veces = 0
while True:
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    entrar,cuantas_veces = login(usuario,clave,cuantas_veces)
    if not entrar:
        print("Error. Nombre de usuario o contraseña incorrecta")
    if entrar or cuantas_veces == 3:
        break
if entrar:
    print("Bienvnidos al sistema")
else:
    print("No has entrado en el sistema")
