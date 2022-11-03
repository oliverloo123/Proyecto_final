print("===CLAVE===")
nombre = input("Ingrese su nombre: \r\n")
nombre_articulo = input("Ingrese el nombre del articulo: \r\n")
precio = int(input("Ingres el precio: \r\n"))
print ("[1].Clave")
print ("[2].Clave")
print ("[3].Salir")
clave = int(input("Ingresesu clave:"))
if clave == 1:
    descuento = precio * 0.1
    precio_total = precio - descuento
    print("El nombre de su producto es: ", nombre_articulo)
    print("la clave es: ", clave)
    print("El precio anterios es: ", precio)
    print("Su precio actual es: ", precio_total)
elif clave == 2:
    descuento = precio * 0.2
    precio_total = precio - descuento
    print("El nombre de su producto es: ", nombre_articulo)
    print("la clave es: ", clave)
    print("El precio anterios es: ", precio)
    print("Su precio actual es: ", precio_total)
elif clave == 3:
    print("Gracias por su visita")
else:
    print("No exite esa opcion")
