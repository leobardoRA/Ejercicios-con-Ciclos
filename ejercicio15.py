# Pedimos al usuario un número entero
numero = int(input("Introduce un número entero: "))

# Convertimos el número a binario usando la función bin() y eliminamos el prefijo '0b'
numero_binario = bin(numero)[2:]

# Mostramos el número en binario
print(f"El número {numero} en binario es: {numero_binario}")

