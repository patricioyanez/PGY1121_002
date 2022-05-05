# 1.- Crear variables
total = 0
# 2.- Solicitar los datos al usuarios
print("\n***** Venta de Artículos *****")

mascarillas = int(input("Cantidad de mascarillas: "))
guantes     = int(input("Cantidad de guantes    : "))
delantal    = int(input("Cantidad de delantal   : "))
amonio      = int(input("Cantidad de amonio     : "))
cupon       = int(input("Tiene nro Cupón        : "))
 
# 3.- Procesarlos

total += mascarillas * 1000 #  total = total + mascarillas * 1000
total += guantes * 1000
total += delantal * 2000
total += amonio * 3000

if cupon > 0:
    descuento = int(input("Ingrese % de descuento:"))
    total -= total * descuento / 100
# 4.- Mostrar los resultados

print("El total a pagar es:", total)