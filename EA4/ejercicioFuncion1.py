def resta(a =None, b=None):
    if a == None or b == None:
        print("Error en los datos")
        return # finalizar la ejecución de la función
    return a - b

resta()
resta(1)
print(resta(4,1))