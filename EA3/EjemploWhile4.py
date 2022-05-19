total = 0
opcion= 0

while opcion != 6:
    print("======  Panadería DuocUC  ======")
    print("1.- Pan Amasado")
    print("2.- Pan Molde")
    print("3.- Pan Baguette")
    print("4.- Pan Integral")
    print("5.- Total de compra")
    print("6.- Salir")
    try:
        opcion = int(input("Ingrese una opción:"))
    except:
        print("Error en al opción ingresada")

    if opcion < 1 or opcion > 6:
        print("Opción no válida")
        input("Presione enter para continuar")
    elif opcion == 6:
        print("Aplicación cerrada")
    elif opcion == 5:
        if total < 5000:
            total *= 1.1
        else:
            print("Envio gratis")
        print("El total de la compra es:",int(total))
        total = 0
        input("Presione enter para continuar")

    else:
        try:
            cantidad = int(input("Ingrese cantidad:"))
        except:
            print("Error en la cantidad ingresada")
            continue
        
        if opcion == 1:
            total += cantidad * 1500
        elif opcion == 2:
            total += cantidad * 1000
        elif opcion == 3:
            total += cantidad * 2000
        elif opcion == 4:
            total += cantidad * 3000
            