# descargar la libreria numpy
# consola -> pip install numpy
# para verificar si esta instalado pip list
import numpy as nu
casillero = nu.array([  ["","",""],
                        ["","",""],
                        ["","",""] ])

# definir las funciones
def arrendar(casillero):
    pass
def mostrarCasillerosFila(casillero, fila):
    pass
def mostrarDisponible(casillero):
    pass
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