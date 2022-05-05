nota1 = input("Ingrese nota 1: ")
nota2 = input("Ingrese nota 2: ")
nota3 = input("Ingrese nota 3: ")

# convirtir las notas a numeros
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

if nota1 < 1 or nota1 > 7:
    print("La nota 1 no es válida")
elif nota2 < 1 or nota2 > 7:
    print("La nota 2 no es válida")
elif nota3 < 1 or nota3 > 7:
    print("La nota 3 no es válida")
else:
    promedio = (nota1 + nota2 + nota3) / 3 
    print("Su promedio es: ", "{:0.1f}".format(promedio))

    if promedio < 4:
        print("Reprobó :(")
    else:
        print("Aprobó felicidades")