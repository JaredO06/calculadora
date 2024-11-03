Simulación de una Máquina de Galton

Este proyecto simula una máquina de Galton en Python, generando una distribución de las posiciones finales de canicas que caen a través de una serie de obstáculos. La simulación muestra cómo las canicas se acumulan en diferentes contenedores, siguiendo una distribución binomial que se aproxima a una campana de Gauss.

Descripción del Proyecto

La máquina de Galton es un dispositivo que permite observar cómo las canicas, al caer a través de una serie de niveles de obstáculos, se distribuyen de forma aproximada en una curva de campana. En
esta simulación:3,000 canicas caen a través de 12 niveles.
Cada canica tiene una probabilidad del 50% de desviarse hacia la izquierda o hacia la derecha en cada nivel.
Al final, un histograma muestra la cantidad de canicas en cada contenedor, representando la distribución final de las posiciones.

Estructura del Código

El programa está dividido en dos funciones principales:

Función simular_galton:

Propósito: Simula la caída de las canicas a través de la máquina de Galton.

Parámetros:
num_canicas: Número total de canicas que caen (en este caso, 3000).
num_niveles: Número de niveles de obstáculos (en este caso, 12).

Proceso:

Para cada canica, la función genera una serie de decisiones aleatorias (izquierda o derecha) en cada nivel.
La posición final de cada canica se calcula sumando las decisiones de cada nivel, y el resultado se almacena en un array.

Salida: Un array con la posición final de cada canica, indicando en qué contenedor cayó.

Función graficar_histograma:

Propósito: Genera un histograma de los resultados obtenidos en la simulación.

Parámetros
resultados: Array con la posición final de cada canica (generado por simular_galton).

num_niveles: Número de niveles en la máquina de Galton.

Proceso
Crea un histograma utilizando matplotlib, donde el eje X representa los contenedores y el eje Y la cantidad de canicas en cada contenedor.
Incluye etiquetas en los ejes y un título descriptivo.
