# 1.- Crear variables
# 2.- Solicitar los datos al usuarios
print("\n***** Comparación de 3 números *****")
n1 = input("Ingrese 1er valor: ")
n2 = input("Ingrese 2do valor: ")
n3 = input("Ingrese 3er valor: ")

# 3.- Procesarlos
# 4.- Mostrar los resultados

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print("El 1er nro es el mayor")
elif n2 > n3:
    print("El 2do nro es el mayor")
else:
    print("El 3er nro es el mayor")