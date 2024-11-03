simulacion maquina  de galton
import numpy as np
import matplotlib.pyplot as plt

# Función para simular la caída de las canicas en la máquina de Galton
def simular_galton(num_canicas, num_niveles):
    resultados = np.zeros(num_canicas)  # Array para almacenar la posición final de cada canica
    for i in range(num_canicas):
        # Cada nivel es una decisión hacia la izquierda (0) o la derecha (1)
        decisiones = np.random.randint(0, 2, num_niveles)
        resultados[i] = np.sum(decisiones)  # Sumar las decisiones para obtener la posición final
    return resultados

# Función para graficar el histograma de resultados
def graficar_histograma(resultados, num_niveles):
    plt.hist(resultados, bins=num_niveles + 1, edgecolor='black')
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de canicas')
    plt.title('Simulación de una Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Ejecución de la simulación y graficación de resultados
resultados = simular_galton(num_canicas, num_niveles)
graficar_histograma(resultados, num_niveles)
