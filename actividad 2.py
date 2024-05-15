# Inicialización de la variable sw
sw = 1

# Bucle principal
while sw == 1:
    # Menú principal
    print("\nMenú Principal:")
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")

    try:
        # Selección de opción
        opcion = int(input("Seleccione una opción: "))

        # Validación de entrada
        if opcion < 1 or opcion > 3:
            raise ValueError("Opción inválida. Por favor, seleccione una opción del 1 al 3.")

        # Acciones según la opción
        if opcion == 1:
            print("Tiene un saldo de $500000.")
            confirmacion = int(input("Presione 1 para volver atrás o 2 para salir: "))
            if confirmacion == 2:
                print("Cierre de sesión exitoso, adiós.")
                break
        elif opcion == 2:
            print("Transferencia realizada.")
            confirmacion = int(input("Presione 1 para volver atrás o 2 para salir: "))
            if confirmacion == 2:
                print("Cierre de sesión exitoso, adiós.")
                break
        elif opcion == 3:
            print("Cierre de sesión exitoso, adiós.")
            sw = 0  # Salir del bucle principal
    except ValueError as ve:
        print(ve)