# 1.- Definir variables
contador = 1
total = 0
# 2.- Solicitar la info al usuario
# 3.- Procesar info
print("\n ******=== Suma de 5 números ===******")
while contador <= 5:
    nro = int(input("Ingrese número a sumar:"))
    if nro > 0:    
        total += nro
        contador += 1
# 4.- Mostrar el resultado
print("La suma total es:", total)