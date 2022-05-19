a = 5
b = 10
try:
    print("El resultado es:", (a/b))
except ZeroDivisionError: 
    print("Error: ha dividido por cero")
except:
    print("Error en la ejecución del código")
else:
    print("El bloque TRY no tuvo errores que informar")

print("App cerrada")