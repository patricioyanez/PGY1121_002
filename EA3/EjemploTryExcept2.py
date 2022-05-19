a = 5
b = 0
try:
    print("El resultado es:", (a/b))
except ZeroDivisionError: 
    print("Error: ha dividido por cero")
except:
    print("Error en la ejecución del código")

print("App cerrada")