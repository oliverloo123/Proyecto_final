cad=input("Cadena:")			
lista=cad.split(" ")
for palabra in lista:
  	print(palabra[0],)
print("")
 
for palabra in lista:
  	print(palabra.capitalize(),)
print("")

 
for palabra in lista:
  	if palabra.startswith("a") or palabra.startswith("A"):
  		print(palabra,)