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
        try:
            rut = int(input("Ingrese su rut"))

            if rut < 4000000 or rut > 99999999:
                raise ("El rut no está dentro del rango permitido")
        except:
            print("El rut no es válido")
            input("Presione enter para continuar.....")
            continue

        nombre      = input("ingrese su nombre       : ")
        direccion   = input("ingrese su direccion    : ")
        comuna      = input("ingrese su comuna       : ")
        correo      = input("ingrese su correo       : ")

        if correo.count("@") != 1:
            print("El correo no es válido")
            input("Presione enter para continuar.....")
            continue

        try:
            edad = int(input("Ingrese su edad :"))

            if edad < 0 or edad > 110:
                raise ("La edad no está dentro del rango permitido")
        except:
            print("La edad no es válido") 
            input("Presione enter para continuar.....")
            continue

        genero = input("ingrese su género(F o M): ")

        if not genero in ['F', 'M']:
            print("El género no es válido")            
            input("Presione enter para continuar.....")
            continue

        celular     = input("ingrese su celular      : ")
        tipo        = input("ingrese su tipo: 1.-PREMIUM 2.-GOLD 3.-SILVER:")

        if tipo == "1":
            tipo = "PREMIUM"
        elif tipo == "2":
            tipo = "GOLD"
        elif tipo == "3":
            tipo = "SILVER"
        else:            
            print("El tipo de cliente no es válido") 
            input("Presione enter para continuar.....")
            continue

        cliente = [rut, nombre, direccion, comuna, correo, edad, genero, celular, tipo, suscripcion]
        clientes.append(cliente)

    elif opcion == 2:
        print("Seleccionó la opción 2")
    elif opcion == 3:
        print("Seleccionó la opción 3")

    input("Presione enter para continuar.....")
