def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    return num1 / num2

opcion = 0
listaDeOpciones = ["1", "2", "3", "4", "5"]
while opcion != "5":
    print("====== Calculadora ======")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")

    opcion = input("Ingrese una opción:")

    if opcion not in listaDeOpciones:
        print("La opción no es válida.")
        input("Presione enter para continuar....")
        continue
    
    if opcion == "5":
        print("Adiós!!! :)")
    else:
        resultado = ""
        num1 = 0 
        num2 = 0
        try:
            num1 = int(input("Ingrese número 1:"))
            num2 = int(input("Ingrese número 2:"))
        except:
            print("Valores no son válidos.")
            input("Presione enter para continuar....")
            continue


        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)
        
        print("El resultado es:", resultado)
        input("Presione enter para continuar....")
