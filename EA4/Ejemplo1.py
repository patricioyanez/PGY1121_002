import numpy
arreglo = numpy.array([2,3,6,8,9,21,23,5,6,70])
print(arreglo)

print("Cantidad de elementos    :", arreglo.shape)
print("Cantidad de elementos    :", len(arreglo))
print("Cantidad de dimensiones  :", arreglo.ndim)


# Acceder a los valores de un arreglo
print("El 1er valor es:", arreglo[0])
print("El 2do valor es:", arreglo[1])

# accede a los ultimos elementos mediante indice negativo
print("El último valor es:", arreglo[-1])
print("El peúltimo valor es:", arreglo[-2])
print("El ante peúltimo valor es:", arreglo[-3])

# permite obtener una porción del arreglo
print("Los valores son:", arreglo[4:8])
print("Los valores son:", arreglo[4:])
print("Los valores son:", arreglo[:5])
print("Los valores son:", arreglo[1:8:2])
print("Los valores son:", arreglo[::4])
print("Los valores son:", arreglo[6::3])
print("Los valores son:", arreglo[:5:2])
