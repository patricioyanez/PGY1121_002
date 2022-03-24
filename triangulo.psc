Algoritmo triangulo
	Definir lado1 Como Entero
	Definir lado2 Como Entero
	Definir lado3 Como Entero
	
	Escribir "Ingrese el 1er lado"
	Leer lado1
	Escribir "Ingrese el 2do lado"
	Leer lado2
	Escribir "Ingrese el 3er lado"
	Leer lado3
	
	si lado1 = lado2 y lado1 = lado3 Entonces
		Escribir "Equilatero"
	SiNo
		si lado1 = lado2 o lado1 = lado3 o lado2 = lado3 Entonces
			Escribir "Isoceles"
		SiNo
			Escribir "Escaleno"
		FinSi
	FinSi
	
FinAlgoritmo
