clientes = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo = ""
suscripcion = True

opcion = 0

while opcion != 4:
    print(" ***** M E N Ú *****")
    print("1.- Ingresar cliente")
    print("2.- Suscribir")
    print("3.- Consultar")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except:
        print("Opción no es válida")
        input("Presione enter para continuar.....")
        continue
    
    if opcion < 1 or opcion > 4:
        print("Opción no existe")
        input("Presione enter para continuar.....")
        continue
    
    if opcion == 4:
        print("Adiós :)")
    elif opcion == 1:
        print("Seleccionó la opción 1")
    elif opcion == 2:
        print("Seleccionó la opción 2")
    elif opcion == 3:
        print("Seleccionó la opción 3")

    input("Presione enter para continuar.....")
