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
