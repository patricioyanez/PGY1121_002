numero = 5
numero = numero + 5
print("El resultado es", numero) # permite enviar mensaje a la consola

print("Ingrese su nombre:")
nombre = input() # permite capturar datos desde el teclado
print("Su nombre es:", nombre)

apellido = input("Ingrese su apellido: ")
print("Su nombre completo es:", nombre, apellido)

anio = input("Ingrese su año de nacimiento: ")
edad = 2022 - int(anio)  # funcion int() convierte un texto con nro en un int
print("Ud tiene: ", edad, "años")

# concatenar str con int
mensaje = "Ud tiene " + str(edad) + " años" # str convierte el valor a un texto
print(mensaje)