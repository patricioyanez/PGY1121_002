print("***** Convertido de moneda extranjera a peso *****")
print("=== menú de monedas disponibles ===")
print("1.- Dolar Australianos")
print("2.- Pesos Argentinos")
print("3.- Yen")
opcion = input("Ingrese opción: ")

cantidad = input("Ingrese cantidad de la moneda: ")
cantidad = float(cantidad)
total = 0
if opcion == "1":
    valor = input("Ingrese valor actual del valor del Dolar Autraliano: ")
    total = float(valor) * cantidad
    print("El total en pesos es: $", int(total) )
elif opcion == "2":
    valor = input("Ingrese valor actual del valor del Peso Argentino: ")
    total = float(valor) * cantidad
    print("El total en pesos es:v$", int(total) )
elif opcion == "3":
    valor = input("Ingrese valor actual del valor del Yen: ")
    total = float(valor) * cantidad
    print("El total en pesos es: $", int(total) )
else:
    print("La opción no es válida :(")
