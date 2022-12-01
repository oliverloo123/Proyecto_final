#libreria para hacer grafico.

import tkinter as tk
ventana = tk.Tk()

#Hce poner el titulo de la ventana 
ventana.title("Ejemplo")

#La dimencion de la vntana que has creado
ventana.geometry("400x400")

#Camabio el color de las palabras
label = tk.Label(text="Ventana de ideas", bg="black",fg="red")

#Afecta la posicion del cuadrada de las letras
label.grid(row=0,column=0)

#LO coloca al centro a los dos depende de las cordenadas
entry = tk.Entry(width=70)

entry.grid(row=2,column=0)

boton = tk.Button(text="Enviar",width=100)

#Afecta l posicion de la linea blanca 
entry.grid(row=2,column=0)

ventana.mainloop()