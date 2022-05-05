Algoritmo EjercicioSueldo
	Definir sueldo1 Como Entero
	Definir sueldo2 Como Entero
	Definir sueldo3 Como Entero
	
	Escribir "Ingrese 1er sueldo"
	Leer sueldo1
	Escribir "Ingrese 2do sueldo"
	Leer sueldo2
	Escribir "Ingrese 3er sueldo"
	Leer sueldo3
	
	si sueldo1 > sueldo2 Entonces 
		si sueldo1 > sueldo3 Entonces
			Escribir "El sueldo 1 es el mayor $", sueldo1
		sino 
			Escribir "El sueldo 3 es el mayor $", sueldo3 
		FinSi
	SiNo
		si sueldo2 > sueldo3 Entonces
			Escribir "El sueldo 2 es el mayor $", sueldo2
		sino 
			Escribir "El sueldo 3 es el mayor $", sueldo3 
		FinSi
	FinSi
	// otra forma de resolver el caso
	si sueldo1 > sueldo2 y sueldo1 > sueldo3 Entonces 
		Escribir "El sueldo 1 es el mayor $", sueldo1
	SiNo
		si sueldo2 > sueldo3 Entonces
			Escribir "El sueldo 2 es el mayor $", sueldo2
		SiNo
			Escribir "El sueldo 3 es el mayor $", sueldo3 
		FinSi
	FinSi
	
	
	
FinAlgoritmo
