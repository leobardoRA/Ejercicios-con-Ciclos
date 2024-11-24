# Inicializamos la variable para el total pagado
total_pagado = 0

# Recorremos los 20 meses
for mes in range(1, 21):
    # El pago de cada mes es 10 euros por el número del mes
    pago_mes = 10 * mes
    
    # Sumamos lo pagado en este mes al total
    total_pagado += pago_mes
    
    # Mostramos el pago del mes actual
    print(f"Mes {mes}: {pago_mes} euros")

# Imprimimos el total pagado después de 20 meses
print(f"\nTotal pagado después de 20 meses: {total_pagado} euros")
