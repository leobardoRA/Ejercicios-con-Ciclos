# Función para verificar si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Comprobamos hasta la raíz cuadrada de num
        if num % i == 0:
            return False
    return True

# Pedimos al usuario la cantidad de números primos que quiere mostrar
cantidad = int(input("¿Cuántos números primos deseas mostrar? "))

# Inicializamos una lista para almacenar los números primos encontrados
primos = []
numero = 2  # El primer número primo es 2

# Buscamos los primeros N números primos
while len(primos) < cantidad:
    if es_primo(numero):
        primos.append(numero)
    numero += 1

# Mostramos los N primeros números primos
print(f"Los primeros {cantidad} números primos son: {primos}")
