# 1.- definir variables
acumulador = 0
contador = 0

# 2.- Solicitar la información al usuario
print("****** Ingrese 3 numeros ******")
n1 = input("Ingrese número 1:")
n2 = input("Ingrese número 2:")
n3 = input("Ingrese número 3:")

# 3.- Procesar la info obtenida
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > 0 and n1 % 2 == 0:
    acumulador += n1 # acumulador = acumulador + n1
else:
    contador += 1 # contador = contador + 1

if n2 > 0 and n2 % 2 == 0:
    acumulador += n2 
else:
    contador += 1 
    
if n3 > 0 and n3 % 2 == 0:
    acumulador += n3 
else:
    contador += 1 

# 4.- Mostrar los resultados
print("La suma de los numero es     :", acumulador)
print("La cuenta de los numeros es  :", contador)
###  Realizar los demás ejercicios de la ppt como tarea
## inscibirse a el curso de cisco :)