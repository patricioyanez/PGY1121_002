import numpy as num

arreglo = num.arange(10) # 0 - 9 
print(arreglo) 
arreglo = num.arange(10.0) 
print(arreglo)
arreglo = num.arange(4, 10) 
print(arreglo)
arreglo = num.arange(2, 21, 2) 
print(arreglo)
arreglo = num.arange(1, 21, 2) 
print(arreglo)

## arreglo como objeto
var = arreglo
var[0]= 100
print(arreglo[0])

var1 = arreglo.copy()
var1[0]= 555
print(arreglo)
print(var)
print(var1)




