def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(opcion, numero1, numero2):
    if opcion == 1:
        return sumar(numero1, numero2)

    elif opcion == 2:
        return restar(numero1, numero2)

    elif opcion == 3:
        return multiplicar(numero1, numero2)

    elif opcion == 4:
        return dividir(numero1, numero2)

    else:
        return "Opción inválida"


print("=== CALCULADORA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")


opcion = int(input("Seleccione una opción: "))

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultado = calcular(opcion, numero1, numero2)

print("Resultado:", resultado)
