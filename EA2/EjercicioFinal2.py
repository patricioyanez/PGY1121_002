# 1.- Crear variables
# 2.- Solicitar los datos al usuarios
print("\n***** Registro de datos *****")
nombre = input("Ingrese su nombre                   : ")
edad = input("Ingrese su edad                     : ")
telefono = input("Ingrese su teléfono                 : ")
genero = input("Ingrese su género 1.-Varón 2.-Mujer : ")

# 3.- Procesarlos
# 4.- Mostrar los resultados

if genero == "1": # if int(genero) == 1:
    print(f"Nombre: {nombre} y su edad es {edad}")
else:
    print("Nombre:", nombre, " y su teléfono es", telefono)