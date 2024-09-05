# Función para validar que la entrada no esté vacía
def validar_texto(texto):
    while not texto.strip():  # Repite hasta que el texto no esté vacío
        texto = input("Este campo no puede quedar vacío. Por favor, ingresa nuevamente: ")
    return texto

# Función para validar que la entrada sea un número flotante o entero válido
def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))  # Intenta convertir la entrada a un número flotante
            return valor
        except ValueError:
            print("Por favor, introduce un número válido.")

# Solicitar los datos del usuario con validación
nombre = validar_texto(input("Ingresa tu nombre: "))
apellido_paterno = validar_texto(input("Ingresa tu apellido paterno: "))
apellido_materno = validar_texto(input("Ingresa tu apellido materno: "))
edad = validar_numero("Ingresa tu edad: ")
peso = validar_numero("Ingresa tu peso en kilogramos: ")
estatura = validar_numero("Ingresa tu estatura en metros: ")

# Calcular el IMC
imc = peso / (estatura ** 2)

# Desplegar la información
print("\n--- Datos del Usuario ---")
print(f"Nombre Completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso:.2f} kg")
print(f"Estatura: {estatura:.2f} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

