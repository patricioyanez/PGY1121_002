try:
    numero = int(input("ingrese un nro"))
    if not type(numero) is int:
        raise("El tipo de dato no es el esperado")
except:
    print("Error en el tipo de datos ingresado")
print("fin de la app")