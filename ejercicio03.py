# Inicialización del acumulador y contador
suma = 0
contador = 0

# Bucle para pedir números hasta que se ingrese un cero
while True:
    # Pedir al usuario que ingrese un número
    numero = int(input("Introduce un número (0 para terminar): "))
    
    # Si el número es cero, salir del bucle
    if numero == 0:
        break
      # Acumular el número en la suma
    suma += numero
    
    # Incrementar el contador
    contador += 1

# Verificar que el contador sea mayor que cero para evitar división por cero
if contador > 0:
    # Calcular la media
    media = suma / contador
    print(f"La suma de los números introducidos es: {suma}")
    print(f"La media de los números introducidos es: {media}")
else:
    print("No se introdujeron números.")
