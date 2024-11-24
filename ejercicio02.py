# Número máximo de intentos
intentos_maximos = 10
intentos_restantes = intentos_maximos

# Mensaje de bienvenida
print("¡Bienvenido al juego de adivinar el número!")
print("He generado un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")

# Bucle para que el usuario intente adivinar el número
while intentos_restantes > 0:
    # Pedir un número al usuario
    intento = int(input(f"Te quedan {intentos_restantes} intentos. Introduce tu suposición: "))
    
    # Comprobar si el intento es correcto
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en {intentos_maximos - intentos_restantes + 1} intentos.")
        break
    elif intento < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
    # Reducir el número de intentos restantes
    intentos_restantes -= 1

# Si se agotaron los intentos, mostrar el número generado
if intentos_restantes == 0:
    print(f"Lo siento, no has adivinado el número. El número correcto era {numero_aleatorio}.")
