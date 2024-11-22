# Función para calcular el factorial
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Solicitar un número al usuario
numero = int(input("Introduce un número para calcular su factorial: "))

# Comprobar si el número es negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    # Calcular y mostrar el factorial
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es {resultado}.")