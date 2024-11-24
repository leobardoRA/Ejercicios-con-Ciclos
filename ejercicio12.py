# Inicializamos la variable para llevar el total ahorrado
total_ahorrado = 0

# Recorremos cada mes (12 meses en total)
for mes in range(1, 13):
    # Pedimos al usuario cuánto ahorra en este mes
    deposito_mes = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
    
    # Añadimos lo depositado en este mes al total ahorrado
    total_ahorrado += deposito_mes
    
    # Mostramos cuánto lleva ahorrado hasta el mes actual
    print(f"Total ahorrado hasta el mes {mes}: {total_ahorrado:.2f}")

# Al final del año, mostramos cuánto ha ahorrado en total
print(f"\nTotal ahorrado en el año: {total_ahorrado:.2f}")
