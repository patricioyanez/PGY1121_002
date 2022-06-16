# descargar la libreria numpy
# consola -> pip install numpy
# para verificar si esta instalado pip list
import numpy as nu
casillero = nu.array([  ["","",""],
                        ["","",""],
                        ["","",""] ], dtype=object)

# definir las funciones
def arrendar(casillero):
    print("**** Arriendo de casillero ****")
    print("Ingrese nivel del casillero")
    print("Nivel 1: $10.000")
    print("Nivel 2: $ 5.000")
    print("Nivel 3: $ 2.000")

    try:
        nivel = int(input("Ingrese nivel del casillero: "))
        fila = nivel - 1
        mostrarCasillerosFila(casillero, fila)
        nroCasillero = int(input("Ingrese el nro de casillero: "))
        columna = nroCasillero - 1
        nombre = input("Ingrese su nombre          : ")
        casillero[fila, columna] = nombre.upper()
#        print(casillero)
    except:
        print("Valor ingresado no es válido.")
        input("Presione enter para continuar....")


def mostrarCasillerosFila(casillero, fila):
    # muestra los casilleros disponibles en la fila enviada
    nroCasillero = 1
    print("Casilleros disponibles de la fila:", fila+1)
    for columna in casillero[fila]:
        if columna == "":
            print("nro de casillero:", nroCasillero, "\n")
        nroCasillero += 1

def mostrarDisponible(casillero):
    print("*** Disponibilidad de los casilleros ***")
    filas = ""
    nroCasillero = 1
    valor = ""

    for fila in casillero:
        for columna in fila:
            if columna == "":
                valor = str(nroCasillero)
            else:
                valor = "X"
            filas += valor + " "
            nroCasillero += 1
        filas += "\n"
    print(filas)
    input("Presione enter para continuar....")


def listarCliente(casillero):
    pass
def mostrarGanancia(casillero):
    pass



opcion = 0
listaDeOpciones = ["1", "2", "3", "4", "5"]
while opcion != "5":
    print("====== Menú principal ======")
    print("1.- Arrendar")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Ver nombres de los clientes")
    print("4.- Mostrar ganancias")
    print("5.- Salir")

    opcion = input("Ingrese una opción:")

    if opcion not in listaDeOpciones:
        print("La opción no es válida.")
        input("Presione enter para continuar....")
        continue
    
    if opcion == "5":
        print("Adiós!!! :)")
    else:
        if opcion == "1":
            arrendar(casillero)
        elif opcion == "2":
            mostrarDisponible(casillero)
        elif opcion == "3":
            listarCliente(casillero)
        elif opcion == "4":
            mostrarGanancia(casillero)