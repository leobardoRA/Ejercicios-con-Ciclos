# Pedimos al usuario la base (número real) y el exponente (entero positivo)
base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

# Inicializamos el resultado como 1
resultado = 1

# Si el exponente es positivo, calculamos la potencia multiplicando la base
for i in range(exponente):
    resultado *= base

# Imprimimos el resultado
print(f"El resultado de {base} elevado a la potencia {exponente} es: {resultado}")
