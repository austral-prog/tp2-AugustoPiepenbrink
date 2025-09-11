def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nVuelto\n")
    print("Pesos:")
    vuelto = int(money - expense)
    print(vuelto)
    print("Centavos:")
    centavos = int(money * 100 - expense * 100 - vuelto * 100)
    print(centavos)
