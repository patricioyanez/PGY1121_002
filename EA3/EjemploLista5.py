lista1 = [2,1,5,4,3]

for numero in lista1:
    print(numero)

print("Nros impares")
for numero in lista1:
    if numero % 2 != 0:
        print(numero)


print("Nros pares")
for numero in lista1:
    if numero % 2 == 0:
        print(numero)