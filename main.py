"""
SUMAR
RESTAR
MULTIPLICAR 
DIVIDIR
"""

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

encender = True
operadores = ["+", "-", "*", "/"]

while encender:
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    operador = input('Ingrese su operación matematica o escriba "salir" para cerrar\nsumar(+), resta(-), multiplicación(*) y division(/): ')

    if operador.lower() == "salir":
        encender = False

    elif operador in operadores:
        if operador == "+":
            print("Resultador de la suma:", sumar(num1, num2))
        elif operador == "-":
            print("Resultador de la resta:", restar(num1, num2))
        elif operador == "*":
            print("Resultador de la multiplicación:", multiplicar(num1, num2))
        elif operador == "/":
            if num2 != 0:
                print("Resultador de la division:", dividir(num1, num2))
            else:
                print("No se puede dividir por", num2)

    else:
        print("Error, eliga uno de los 4 operadores")
