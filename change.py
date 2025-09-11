def change():
    expense = 23.75
    money = 100
	print("Ingresar gasto:")
	print(expense)
	print("Dinero recibido")
	print("\nVuelto\n")
	print("Pesos")
	vuelto = int(money-expense)
	print(vuelto)
	print("Centavos:")
	centavos = ((money - expense) -vuelto) * 100
	print(int(centavos))
