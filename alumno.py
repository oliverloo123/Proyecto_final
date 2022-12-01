from ast import Expression
import os

CARPETA = " usuario/ " # carptea de usuiro
EXTENSION = '.txt' #Extencion de archivos

#Datos
class Usuario:
    def _init_(self,nombre,dni,lugar):
        self.nombre = nombre
        self.dni = dni
        self.lugar = lugar

def app():
    #Revisar si la carpteta exite
    crear_biblioteca()

    #Mostrar el menu de opciones
    mostrar_menu()

    #Preguntar al usuario la acion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)
        
        #Ejercutar la opcion
        if opcion == 1:
            agregar_usuario()
            preguntar = False
        


def agregar_usuario():
    print('Escriba los datos correctos para crear tu usuario')
    nombre_usuario = input('Nombre del usuario:  \r\n')

    #Revisar si el contacto ya existe antes de crearlo
    existe = os.path.isfile(CARPETA + nombre_usuario + EXTENSION)

    if not existe:
        with open(CARPETA + nombre_usuario + EXTENSION, 'w') as archivo:
            #Resto de los campos
            dni_usuario = input('Agrega su DNI: \r\n')
            lugar_usuario = input('Agregar su lugar de domicilio: \r\n')
    
            #Insertar la clase

            usuario = Usuario(nombre_usuario, dni_usuario, lugar_usuario)

            #Escribir en el archivo
            archivo.write('Nombre: ' + usuario.nombre + '\r\n')
            archivo.write('DNI: ' + usuario.dni + '\r\n')
            archivo.write('Lugar: ' + usuario.lugar + '\r\n')

            #Mostrar un mensaje de exito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print("Ese contacto ya exite")
    #Riniciar la app
    app()
    


def mostrar_menu():
    print("Seleccione del Menú lo que desea hacer: ")
    print("1) Agregar usuario.")
    print("2) Libro que desea adquirir.") 
    print("3) Comprar o prestar.")
    print("4) Dia de entrega.")
    print("5) Hora de entrega.")
    


def crear_biblioteca():

    if not os.path.exists(CARPETA):
        #crar una carpeta
        os.makedirs(CARPETA)
app()