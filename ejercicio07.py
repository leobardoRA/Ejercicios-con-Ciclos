# Bucle para pedir caracteres hasta que se ingrese un espacio
while True:
    # Pedimos un carácter al usuario
    caracter = input("Ingresa un carácter: ")

    # Si el carácter ingresado es un espacio, terminamos el programa
    if caracter == " ":
        print("Programa terminado.")
        break

    # Verificamos si el carácter es una vocal
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("VOCAL")
    else:
        print("NO VOCAL")
