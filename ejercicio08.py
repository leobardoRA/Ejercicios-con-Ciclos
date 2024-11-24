# Pedimos al usuario que ingrese dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Aseguramos que el rango esté ordenado (de menor a mayor)
if numero1 > numero2:
    numero1, numero2 = numero2, numero1  # Intercambiamos los valores si es necesario

# Imprimimos los números pares en el rango
print(f"Los números pares entre {numero1} y {numero2} son:")

# Usamos range para iterar por los números entre numero1 y numero2
for i in range(numero1 + 1, numero2):  # Evitamos incluir los límites
    if i % 2 == 0:
        print(i)
