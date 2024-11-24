import math

# Pedir al usuario que ingrese un número
numero = int(input("Introduce un número para verificar si es primo: "))

# Verificamos si el número es menor o igual a 1, en cuyo caso no es primo
if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    # Comprobamos si el número es divisible por cualquier número entre 2 y la raíz cuadrada del número
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break  # No es primo, salimos del bucle

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
