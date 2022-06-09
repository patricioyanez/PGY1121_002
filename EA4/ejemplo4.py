import numpy as num

## comparaciones aritmeticas con arreglos

a1 = num.array([1,2,3,4])
a2 = num.array([1,2,3,4])
a3 = num.array([10,2,3,20])

print("igualdad : ", a1 == a2)
print("igualdad : ", a1 == a3)
print("Mayores  : ", a1 > a3)
print("Menores  : ", a1 < a3)
print("Menores  : ", a1 != a3)

# métodos para estadísticas

print(a1)
print("Suma", a1.sum())
print("valor mayor", a1.max())
print("valor menor", a1.min())
print("Promedio", a1.mean())

print("Suma", sum(a1))
print("valor mayor", max(a1))
print("valor menor", min(a1))


