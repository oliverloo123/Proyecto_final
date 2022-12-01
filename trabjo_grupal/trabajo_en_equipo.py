print("/// BIENVENIDO A LA BIBLIOTECA ///")
print("Por favor elegir correctamente: ")

print("[1]. Administrador")
print("[2]. Cliente.") 

opcion0 = int(input("La opcion que eligio es: \r\n"))


if opcion0 == 1:

    user_ = "admin"
    pwd_ = "pepe grillo"
    print("===Bienvenido===")
    print("Ingrese sus datos: ")
    print("Usuario: ")
    user = input()
    print("Contraseña:")
    pwd = input()

    while user==user_ and pwd==pwd_:
        print("Bienvenido al programa: ")

        print("Seleccione una opcion:")

        print("[1]. Agregar libro.")
        print("[2]. Borrar libro.")
        print("[3]. Reemplazar precios.")
        print("[4]. Agregar diversos libros")
        print("[5]. Salir")

        opcion = int(input('La opcion es: \r\n'))

        if opcion == 1:
            print("Agregue el nuevo libro: ")
            print("Elija las opciones de libros disponibles para la biblioteca")
            agregar_nombres_de_libros = ["Divina comedia", "Hamlet", "Edipo rey", "Rojo y negro", "El idiota", "Antes de diciembre"]
            print(agregar_nombres_de_libros)
    
            Libro = input("= ")

            if Libro == agregar_nombres_de_libros[0] or Libro == agregar_nombres_de_libros[1] or Libro == agregar_nombres_de_libros[2] or Libro == agregar_nombres_de_libros[3] or Libro == agregar_nombres_de_libros[4] or Libro == agregar_nombres_de_libros[5]:
                print("Libros que seran agregados ")

                print("* AUTORES *")

                autores = ["Dante Alighieri", "William Shakespeare", "Sófocles", "Stendhal", "Fiódor Dostoievski", "Joana Marcús"]
                print(autores)

                autor = input("Ingresa el nombre del autor: \r\n")

                if autor == autores[0] or autor == autores[1] or autor == autores[2] or autor == autores[3] or autor == autores[4] or autor == autores[5]:
                    print("El autor y libro que ha seleciondo es correcto")
                    print("Buena eleccion ya esta agregado el libro")
                    
                else:
                    print("El autor o libro no existe")
                    print("Intentalo de nuevo")


        elif opcion == 2:
            print("Seleccione el libro que desea borrar: ")

            elimar_nombres_de_libros = ["Almas muertas", "Cien años de soledad", "Orgullo y prejuicio", "Don Quijote de la Mancha", "Crimen y castigo", "El señor de los anillos"] 
            print(elimar_nombres_de_libros)

            elimiar = input("= ")

            if elimiar == elimar_nombres_de_libros[0] or elimiar == elimar_nombres_de_libros[1] or elimiar == elimar_nombres_de_libros[2] or elimiar == elimar_nombres_de_libros[3] or elimiar == elimar_nombres_de_libros[4] or elimiar == elimar_nombres_de_libros[5]:
                print("El libro sera eliminado ")

                print("* AUTORES *")

                autores = ["Nikolai Gogol", "Gabriel García Márquez", "Jane Austen", "J. R. R. Tolkien", "Fiódor Dostoyevski", "Miguel de Cervante"]
                print(autores)

                autor = input("Ingrese el nombre del autor: \r\n")
 
                if autor == autores[0] or autor == autores[1] or autor == autores[2] or autor == autores[3] or autor == autores[4] or autor == autores[5]:
                    print("El autor y libro se han eliminado exitosamente")
            
                else:
                    print("El autor o libro no existe")
                    print("Intentalo de nuevo")
        

        elif opcion == 3:
            print("Seleccione el libro que desea cambiar de precio: ")
            cambiar_precio = ["Almas muertas","Cien años de soledad","Orgullo y prejuicio","Don Quijote de la Mancha","Crimen y castigo","El señor de los anillos","Divina comedia","Hamlet","Edipo rey","Rojo y negro","Guerra y paz","Antes de diciembre"]
            print(cambiar_precio)
          
            eliminar = input("Ingrese el nombre del libro: ")
         

            if eliminar == cambiar_precio[0] or eliminar == cambiar_precio[1] or eliminar == cambiar_precio[2] or eliminar == cambiar_precio[3] or eliminar == cambiar_precio[4] or eliminar == cambiar_precio[5] or eliminar == cambiar_precio[6] or eliminar == cambiar_precio[7] or eliminar == cambiar_precio[8] or eliminar == cambiar_precio[9]or eliminar == cambiar_precio[10] or eliminar == cambiar_precio[11]:
                
                print("Cambiara el precio del libro ")

                print("*  *")

                autores = ["20$", "40$", "50$", "60$", "65$", "80$"]
                print(autores)

                autor = input("Ingrese el precio por el cual quiere reemplazar: \r\n")
 
                if autor == autores[0] or autor == autores[1] or autor == autores[2] or autor == autores[3] or autor == autores[4] or autor == autores[5]:
                    print("El libro ", eliminar, " cambio de precio exitosamante a ", autor)
            
                else:
                    print("El autor o libro no existe")
                    print("Intentalo de nuevo")
                    

        elif opcion == 4: 
                x=["Se agregaron: "]
                print("Ingrese la cantidad de libros que desee: ")
                print("Almas muertas, Cien años de soledad, Orgullo y prejuicio, Don Quijote de la Mancha, Crimen y castigo, El señor de los anillos, Divina comedia, Hamlet, Edipo rey, Rojo y negro, Guerra y paz, Antes de diciembre")
                n = int(input("Cantidad de libros y los libros: "))
                for i in range(0,n):
                    x.append(input())
                print(x)

                print("Excelente, se agrego correctamente el libro, gracias.")
    else: 
      print("Usuario o contraseña incorrecta")

    

while opcion0 == 2:
    print("/// MENÚ DE LA BIBLIOTECA ///")

    print("Seleccione una opcion por favor")

    print("[1]. Agregar usuario.")
    print("[2]. Libro que desea adquirir.") 
    print("[3]. Comprar o prestar.")
    print("[4]. Dia de entrega.")
    print("[5].Hora de entrega.")
    print("[6]. Salir.")

    opcion = int(input('La opcion es: \r\n'))


    if opcion == 1:
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

 
    elif opcion == 2:
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


    elif opcion == 3:
        print("* MODALIDAD *")
        print("[1].Comprar.")
        print("[2].Prestado.")

        opcion2 = int(input("Su opcion es: \r\n"))

        if opcion2 == 1:
            print("* FORMA DE PAGO *")
            print("[1]. Efectivo.")
            print("[2]. Tarjeta.")

            opcion2_1 = input("Su forma de pago es: \r\n")

            if opcion2_1 == "Efectivo":

                Monto_a_pagar = float(input("Ingrese el moento a pagar: "))
                print("Su eleccion es pagar con efectivo.")
                print("No olvidar pagar")

            elif opcion2_1 == "Tarjeta":
                print("* TIPO DE TARJETA *")
                tipo_de_tarjeta = ["BBV", "Interbank", "Scotiabank", "BCP"]
                print(tipo_de_tarjeta)
                tipo = input("Ingrese el tipo de tarjeta: \r\n")
            
            
                if tipo == tipo_de_tarjeta[0] or tipo == tipo_de_tarjeta[1] or tipo == tipo_de_tarjeta[2] or tipo == tipo_de_tarjeta[3]:
                    Tarjeta = int(input("Ingrese su numero de trajeta : \r\n"))

                    if Tarjeta < 9999999999999999:
                        CVV = int(input("Ingrese el CVV de su tarjeta: \r\n"))

                        if CVV < 999:
                            Monto_a_pagar = float(input("El monto a pagar es de $: \r\n"))

                            if Monto_a_pagar < 999:
                                print("El monto total a pagar es $: ",Monto_a_pagar)  
                                print("Ha completado correctamente y su compra esta realizada")
                            else:
                                print("El monto indicado no exite, intentelo otra vez")

                        else:
                            print("Su CVV es incoreccto vuelve a intentar")

                    else:
                        print("Es incorrecto su numero de tarjeta")

                else:
                    print("No contamos con ese tipo de tarjeta")

        elif opcion2 == 2:

            print("Su opcion fue llevarse prestado el libro de", Libro)
            print("Del autor", autor)

        else:
            print("Esa opcion es incorrecta")


    elif opcion == 4:

        print("* DIAS *")

        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        print(dias)

        dia_semana = input("Ingrese el nombre del dia a recoger: \r\n")

        if dia_semana == dias[0] or dia_semana == dias[1] or dia_semana == dias[2] or dia_semana == dias[3] or dia_semana == dias[4]:
            print("El dia esta disponible para recoger")

        else:
                print("El dia esta inhabilitado")
                print("Intenta de nuevo")


    elif opcion == 5:

        print("* Turnos disponibles *")

        horas = ["Turno Mañana","Turno Tarde","Turno Noche"]
        print(horas)
        
        horas_disponibles = input("La hora seleccionada es :\r\n")
        print(horas_disponibles)

        if horas_disponibles == horas[0] or horas_disponibles == horas[1] or horas_disponibles == horas[2]:
            print("--Turno establecido--")
  
        else: 
            print("La hora seleccionada no existe")
            print("Intentelo otra vez")


    elif opcion == 6:
        dd = int(input("Ingrese el dia: "))
        mm = int(input("Ingrese el mes: "))
        yy = int(input("Ingrese el año: "))

        print("################# BIBLIOTECA EL BOSQUE #######################")
        print("                   AV.Santa Anita 230                         ")
        print("--------------------R.U.C.N° 1000095211-----------------------")
        print("--------------------TICKET DE VENTA---------------------------")
        print( dd , "/" , mm , "/" , yy , "/""-------------------------------")
        print("--------------------------------------------------------------")
        print("####################### BOLETA ###############################")
        print("#################### INFORMACION #############################")
        print("Bienvenido ",                                            nombre)
        print("DNI: ",                                                     DNI)
        print("Edad: ",                                                   edad) 
        print("Domicilio: ",                                             lugar)
        print("--------------------------------------------------------------")
        print("################## ELECCION DE LIBRO #########################")
        print("El libro que ha elgido es: ",                             Libro)
        print("El autor del libro que eligio es: ",                      autor)
        print("--------------------------------------------------------------")
        print("################### METODO DE PAGO ###########################")
        print("Su metodo de pago fue de: ",                          opcion2_1)
        print("Su pedido estara listo el dia ",  dias,     " en la ",    horas)
        print("El monto a pagar es de                 $/",       Monto_a_pagar)
        print( nombre ,"Muchas gracias por comprar con nosotros.")

        break
