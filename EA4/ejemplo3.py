import numpy as num

## operaciones aritmeticas con arreglos

arreglo = num.array([1,2,3,4])
print(arreglo)
arreglo = arreglo + 1
print(arreglo)
arreglo += 1
print(arreglo)
arreglo -= 1
print(arreglo)
arreglo **= 2
print(arreglo)
arreglo **= 3
print(arreglo)

arreglo1 = num.ones(10)
print(arreglo1)
arreglo1 +=4
print(arreglo1)

arreglo2 = num.ones(10)

print("Suma de 2 arreglos:", arreglo1 + arreglo2)
print("Restar de 2 arreglos:", arreglo1 - arreglo2)

arreglo2 +=1
print("Multiplicar con 2 arreglos:", arreglo1 * arreglo2)
print("Exponente con 2 arreglos:", arreglo1 ** arreglo2)

print("Cantidad de elementos del arreglo 1 {} y del 2 {}".format(arreglo1.shape, arreglo2.shape))
