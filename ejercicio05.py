# Inicializamos el contador y el acumulador
contador = 0
acumulador = 0

# Pedimos 10 números al usuario
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))  # Solicita el número y lo convierte a float
    acumulador += numero  # Suma el número al acumulador
    contador += 1  # Incrementa el contador

# Calculamos el promedio
promedio = acumulador / contador

# Imprimimos el resultado
print(f"El promedio de los 10 números ingresados es: {promedio}")
