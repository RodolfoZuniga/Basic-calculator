def suma(a, b):
    return a + b
    
def calculadora():
    print("Calculadora básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponencial")

    
    opcion = int(input("Seleccione la operación (1-5): "))

    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = 0

    
    if opcion == 1:
        resultado = suma(num1, num2)
    elif opcion == 2:
        resultado = resta(num1, num2)
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
    elif opcion == 4:
        resultado = division(num1, num2)
    elif opcion == 5:
        resultado = exponencial(num1, num2)
    else:
        print("Opción no válida.")

    
    print("El resultado es:", resultado)

calculadora()
