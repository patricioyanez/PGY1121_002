import numpy as num
matriz = num.array([ [1,2,3] , [4,5,6] ])

print("Cantidad de elementos    :", matriz.shape)
print("Cantidad de dimensiones  :", matriz.ndim)
print("elementos de dimensión 0 :", len(matriz[0]))

print("El valor de las coordenada 0,1:", matriz[0,1])
print("El valor de las coordenada 1,2:", matriz[1,2])

print(matriz)
print("Suma:", matriz.sum())
print("Mayor:", matriz.max())
print("Menor:", matriz.min())
print("Menor:", matriz.mean())

print(matriz[0])
print(matriz[0][1:2])
print(matriz[1,1:2])
print(matriz[0][-1])
print(matriz[-1][-1])

matriz2 = num.array([[1,2,3,4,5,6,7,8,9,10],[12,3,4,57,1,4,5,78,0,1]])
print(matriz2[1,2:9:3])


