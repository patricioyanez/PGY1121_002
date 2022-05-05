print("*****  Zapatería Duoc  *****")
talla = input("Ingrese la talla de zapato: ")
cantidad = input("Ingrese unidades a comprar: ")

total = 20000 * int(cantidad)

if total <= 40000:
    total += 3000 # total = total + 3000

print("El total es:", total)