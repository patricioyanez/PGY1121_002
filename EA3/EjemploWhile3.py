nro = 0
flag = True

while flag:
    nro = int(input("Ingrese el numero(103 a 987):"))

    if nro >= 103 and nro <= 987:
        flag = False
    else:
        input("El nro ingresado no es válido. Presione enter para continuar")

unidad = int(nro / 100)
decena = int(nro / 10) - unidad * 10
centena= nro - (unidad * 100 + decena * 10)
nro = centena * 100 + decena * 10 + unidad
print("El número invertido es:", nro)
