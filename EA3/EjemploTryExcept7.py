try:
    numero = int(input("ingrese un nro"))  
except ValueError:
    print("Error en el tipo de datos ingresado")
except:
    print("Error en la captura del dato")
print("fin de la app")