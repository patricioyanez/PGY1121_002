# 1.- Definir variables
contador = 1
total = 1
# 2.- Solicitar la info al usuario
print("\n ******=== Calculo de factorial ===******")
nro = int(input("Ingrese número:"))
# 3.- Procesar info
while contador <= nro:
    total *= contador
    contador += 1
# 4.- Mostrar el resultado
print("El factorial es:", total)