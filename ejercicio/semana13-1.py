def centro(cad):
    print(" " * int(40 - (len(cad)/2)),cad)
    print(" " * int(40 - (len(cad)/2)), "=" * len(cad))

mensaje1 = "Un mensaje centrado"
centro(mensaje1)
mensaje2 = "Otro mensaje"
centro(mensaje2)