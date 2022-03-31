Algoritmo sin_titulo
	Definir opcion Como Entero
	opcion = 0
	
	Mientras opcion <> 4 Hacer
		Limpiar Pantalla
		Escribir " ******  Super Menú ******"
		Escribir "1.- Saludar"
		Escribir "2.- Despedirse"
		Escribir "3.- Preguntar como estas"
		Escribir "4.- Salir"
		Escribir "Ingrese una opcion"
		Leer opcion	
		
		si opcion = 1 Entonces
			Escribir "Hola Usuario, me llamo matrix"
			Escribir "Presione cualquier tecla para continuar"
			Esperar Tecla
		FinSi		
		si opcion = 2 Entonces
			Escribir "Chao usuario, vuelva pronto :)  (k)"
			Escribir "Presione cualquier tecla para continuar"
			Esperar Tecla
		FinSi
	FinMientras
	Escribir "Aplicación cerrada"
	
FinAlgoritmo
