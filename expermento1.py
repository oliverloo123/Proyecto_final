def menuart(): 
    print("/// MENÚ DE LA BIBLIOTECA ///")

    print("Seleccione una opcion por favor")

    print("[1]. Agregar usuario.")
    print("[2]. Libro que desea adquirir.") 
    print("[3]. Comprar o prestar.")
    print("[4]. Dia de entrega.")
    print("[5].Hora de entrega.")
    print("[6]. Salir.")


def Agregar_usuario():
    print("----------------------")
    print("* BIENVENIDO *")
    print("----------------------")
    nombre = input("Ingrese su nombre completo: \r\n")
    DNI = int(input("Ingrese su codigo de DNI: \r\n"))

    if DNI < 99999999:
        edad = int(input("Ingrese su edad: \r\n"))
        if edad < 100:
                lugar = input("Ingrese el lugar de su domicilio: \r\n")
                print("Informacion exitosa")
        else:
                print("Edad incorrecta")
    else:
            print("Su DNI es incorrecto vuelva a intentarlo")

def Libro_que_desea_adquirir():
    
    print("* ALMACEN DE LIBROS *")
    print("* LIBROS *")

    nombres_de_libro = ["Almas muertas", "Cien años de soledad", "Orgullo y prejuicio", "Don Quijote de la Mancha", "Crimen y castigo", "El señor de los anillos"]
    print(nombres_de_libro)

    Libro = input("Ingrese el nombre del libro que desea adquirir: \r\n")

    if Libro == nombres_de_libro[0] or Libro == nombres_de_libro[1] or Libro == nombres_de_libro[2] or Libro == nombres_de_libro[3] or Libro == nombres_de_libro[4] or Libro == nombres_de_libro[5]:
        print("si contamos con el libro")

        print("* AUTORES *")

        autores = ["Nikolai Gogol", "Gabriel García Márquez", "Jane Austen", "J. R. R. Tolkien", "Fiódor Dostoyevski", "Miguel de Cervantes"]
        print(autores)

        autor = input("Ingrese el nombre del autor: \r\n")

        if autor == autores[0] or autor == autores[1] or autor == autores[2] or autor == autores[3] or autor == autores[4] or autor == autores[5]:
                print("El autor que ha seleciondo es correcto")
                print("Buena eleccion ya esta reservado el libro")
        else:
                print("El autor no existe")
                print("Intente de nuevo")

    else:
        print("No hay el libro que desea")
        print("Intenta de nuevo")
























while True: 
    menuart() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        Agregar_usuario() 
    elif opc=='2': 
        Libro_que_desea_adquirir() 
    elif opc=='3': 
        comprar()      
    elif opc=='4': 
        vender()             
    elif opc=='5': 
        eliminar() 
    elif opc == "6":
        login()            
    elif opc=='7': 
        print('Adiós') 
        break  