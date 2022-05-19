lista1 = [1,2,3]
print(lista1)
lista1.append(4)
print(lista1)

lista2 = [5,6,7]
lista3 = [8,9,10]

lista1.extend(lista2)
print(lista1)
lista1 += lista3
print(lista1)

lista1.insert(2, "dos")
print(lista1)

lista1.insert(20, "al fin")
print(lista1)

