# Pedimos al usuario la cantidad de números a introducir
cantidad = int(input("¿Cuántos números quieres ingresar? "))

# Inicializamos los contadores para los números mayores, menores e iguales a 0
mayores_que_cero = 0
menores_que_cero = 0
iguales_a_cero = 0

# Solicitamos los números al usuario
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i + 1}: "))  # Leemos el número y lo convertimos a float
    
    # Comprobamos el valor del número y actualizamos los contadores
    if numero > 0:
        mayores_que_cero += 1
    elif numero < 0:
        menores_que_cero += 1
    else:
        iguales_a_cero += 1

# Mostramos los resultados
print(f"\nCantidad de números mayores que 0: {mayores_que_cero}")
print(f"Cantidad de números menores que 0: {menores_que_cero}")
print(f"Cantidad de números iguales a 0: {iguales_a_cero}")
