'''
1. Suma de elemento
2. Promedio
3. Mayor
4. Menor
5. Buscar Elemento
'''
import carpeta.funciones as fun

lista = []
n = int(input("Cantidad de elemntos: "))
i = 0
while i < n:
    x = int(input())
    fun.add(x)
    i+=1

print("Suma de elementos: ", fun.suma())
print("Promedio: ", fun.promedio())
print("El mayor es: ", fun.mayor())
print("El menor: ", fun.menor()) 

