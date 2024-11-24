# Pedimos el límite inferior y superior del intervalo, asegurándonos de que el inferior sea menor que el superior
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
    
    if limite_inferior < limite_superior:
        break  # Si el límite inferior es menor que el superior, salimos del bucle
    else:
        print("El límite inferior debe ser menor que el límite superior. Vuelve a intentarlo.")

# Inicializamos las variables
suma_intervalo = 0
numeros_fuera = 0
limites_iguales = False

# Pedimos números al usuario hasta que se introduzca el número 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    
    if numero == 0:
        break  # Si el número es 0, terminamos el programa
    
    # Verificamos si el número está dentro del intervalo (intervalo abierto)
    if limite_inferior < numero < limite_superior:
        suma_intervalo += numero
    else:
        numeros_fuera += 1
    
    # Comprobamos si hemos introducido el número igual a los límites
    if numero == limite_inferior or numero == limite_superior:
        limites_iguales = True

# Mostramos los resultados
print("\nResultados:")
print(f"La suma de los números dentro del intervalo es: {suma_intervalo}")
print(f"Cantidad de números fuera del intervalo: {numeros_fuera}")
if limites_iguales:
    print("Se ha introducido un número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
