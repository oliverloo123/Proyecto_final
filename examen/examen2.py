print("========================")
print("========EL SUELDO=======")
print("========================")

cantidad = int(input("Ingrese la cantidad: "))
tasa_interes = float(input("Ingrese el monto de la tasa de interes: "))

interes = cantidad * tasa_interes

if interes > 7000:
    print("Felicidades su tasa de interes es $", interes, "supero os 7000")

else:
    print("Lamentablemente su tasa de interes es $", interes, "no supero os 7000")

total = cantidad + interes
print("Su total sumado con los inters es de $", total)
