Algoritmo EjemploDescuento
	Definir totalAPagar Como Entero
	Definir totalCompra Como Entero
	
	Escribir "Ingrese el monto de la compra"
	Leer totalCompra
	
	si totalCompra >= 500 Entonces
		totalAPagar = totalCompra * .7
	SiNo
		si totalCompra >= 200 Entonces
			totalAPagar = totalCompra * .8
		sino
			si totalCompra>= 100 Entonces				
				totalAPagar = totalCompra * .9
			SiNo
				totalAPagar = totalCompra
			FinSi
		FinSi
	FinSi
	Escribir "El total a pagar es $", totalAPagar
	
	
	
FinAlgoritmo
