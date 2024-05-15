# Inicializa los puntos
puntos = 100000

# Bucle principal
while True:
    # Menú
    print("\nBienvenido al sistema de canje:")
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")

    # Solicitar la opción al usuario
    opcion = int(input("Seleccione una opción: "))

    # Opción 1: Ver los puntos
    if opcion == 1:
        print(f"Tienes {puntos} puntos.")

    # Opción 2: Gastar puntos
    elif opcion == 2:
        print("Seleccione el producto a canjear:")
        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de: 25.000 puntos")
        print("3.- Disco duro portátil, valor de: 30.000 puntos")

        # Mostrar los productos disponibles
        continu = int(input("Seleccione el número correspondiente al producto: "))

        # Validar y descontar puntos según el producto seleccionado
        if continu == 1:
            if puntos >= 10000:
                puntos -= 10000
                print(f"Canje exitoso, te quedan {puntos} puntos.")
            else:
                print("No tienes puntos suficientes para este producto.")
        elif continu == 2:
            if puntos >= 25000:
                puntos -= 25000
                print(f"Canje exitoso, te quedan {puntos} puntos.")
            else:
                print("No tienes puntos suficientes para este producto.")
        elif continu == 3:
            if puntos >= 30000:
                puntos -= 30000
                print(f"Canje exitoso, te quedan {puntos} puntos.")
            else:
                print("No tienes puntos suficientes para este producto.")
        else:
            print("Opción inválida.")

    # Opción 3: Salir
    elif opcion == 3:
        print("¡Gracias por usar nuestro sistema!")
        break

    # Opción inválida
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")