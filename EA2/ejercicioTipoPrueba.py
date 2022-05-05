print("******** CINE DUOC  ********")
print("Cliente es de Duoc")
esDeDuoc = input("1.-Si\n2.-No \nSeleccione opcion: ")

print("=== Tipo de entrada ===")
print("1.- Estreno")
print("2.- Normal")
tipoEntrada = input("Seleccione el tipo de entrada: ")
unidadesTipoEntrada = input("Ingrese unidades a comprar: ")


print("=== Palomitas ===")
print("1.- Pequeña")
print("2.- Mediana")
print("3.- Grande")
tamanoPalomita = input("Seleccione el tamaño de palomitas: ")
unidadesPalomitas= input("Ingrese unidades a comprar: ")

print("=== Bebidas ===")
print("1.- Pequeña")
print("2.- Mediana")
print("3.- Grande")
tamanoBebidas = input("Seleccione el tamaño de bebida: ")
unidadesBebidas= input("Ingrese unidades a comprar: ")

## procesar información recolectada
valor = 0
total = 0
if int(tamanoPalomita) == 1: # tamanoPalomita == "1"
    valor = 2500
elif int(tamanoPalomita) == 2:
    valor = 4500
else:
    valor = 7800
## total de las palomitas solicitadas
total = valor * int(unidadesPalomitas)

if int(tamanoBebidas) == 1: # tamanoBebidas == "1"
    valor = 1000
elif int(tamanoBebidas) == 2:
    valor = 1250
else:
    valor = 2000
## total de las palomitas solicitadas
total = total + valor * int(unidadesBebidas)

if tipoEntrada == "1":
    valor = 4800
else:
    valor = 2900

total = total + valor * int(unidadesTipoEntrada)

print("Subtotal      : ", total)
descuento = 0
if esDeDuoc == "1":
    descuento = total * .3

print("Descuento     : ", descuento)
print("total a pagar : ", (total - descuento) )