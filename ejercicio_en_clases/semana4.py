def jugar(intento = 1 ):
    repuesta = input("¿De que color es una naranja? ")
    if repuesta != "naranja":
        if intento < 3:
            print ("\nFallastes! Intento de nuevo")
            intento += 1 
            jugar(intento)
        else:
            print ("\nPerdistes!")
    else:
        print("\nGanates!")
jugar()
