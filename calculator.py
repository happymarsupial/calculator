while True:
    numero1 = float(input("primer número: "))
    numero2 = float(input("segundo número: "))

    operacion = input("operación (+, -, *, /): ")

    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2
    else:
        resultado = "Operación no válida"

    print(f"El resultado es: {resultado}")
    print("-" * 30) # flodea unas lineas para q quede lindo

    continuar = input("¿deseas realizar una nueva operación? (S/N): ").strip().lower()
    
    if continuar == "n":
        print("¡Gracias por usar la calculadora!")
        break
