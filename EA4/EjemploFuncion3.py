def sumar(a,b):
    total = a + b
    print(f"El total es:{total}")

def sumar2(a,b):
    return a + b
    


num1 = int(input("Ingrese nro 1:"))
num2 = int(input("Ingrese nro 2:"))

sumar(num1, num2)
print("El total es:", sumar2(num1, num2))
