
i = 1
nota_total = 0

while i <= 5:
    print("nota", i)
    nota = int(input())

    if nota > 0 & nota <= 20:
         nota_total + nota
    i += 1
promedio = nota_total/5

if promedio > 12:
    print("APROBASTES")
else:
    print("DESAPROBASTES")


