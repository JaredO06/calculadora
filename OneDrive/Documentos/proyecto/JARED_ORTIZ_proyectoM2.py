# Programa para verificar la longitud de una palabra
palabra = input("Ingresa una palabra: ")

# Calculamos la longitud de la palabra
longitud = len(palabra)

# Verificamos si la longitud está dentro del rango adecuado
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")








# Programa para identificar el cuadrante de un punto
x = float(input("Ingresa la coordenada X: "))
y = float(input("Ingresa la coordenada Y: "))

# Verificamos si alguna coordenada es 0
if x == 0 or y == 0:
    print("Ninguna coordenada puede ser 0.")
else:
    # Identificamos el cuadrante según los signos de X e Y
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")
