import random

# Solicitamos al usuario que ingrese el tamaño de las filas para la matriz
filas = int(input("Ingresa el tamaño de filas para la matriz: "))

# Solicitamos al usuario que ingrese el tamaño de las columnas para la matriz
columnas = int(input("Ingresa el tamaño de columnas para la matriz: "))

# Inicializamos la matriz como una lista vacía
matriz = []

# Generamos la matriz (filas)x(columnas) con valores aleatorios entre 1 y 99
for i in range(filas):
    fila = []  # Creamos una lista para la fila actual
    for j in range(columnas):
        num_generado = random.randint(1, 99)
        fila.append(num_generado)  # Añadimos el número generado a la fila actual
    matriz.append(fila)  # Añadimos la fila completa a la matriz

# Mostramos la matriz generada
print("Matriz generada automáticamente:")
for fila in matriz:
    print(" ".join(f"{num:2}" for num in fila))

# Ordenamos la matriz utilizando el método Bubble Sort
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        for k in range(len(matriz[i])-1):
            if matriz[i][k] > matriz[i][k+1]:
                matriz[i][k], matriz[i][k+1] = matriz[i][k+1], matriz[i][k]


# Mostramos la matriz ordenada
print("\nMatriz con filas ordenadas en orden ascendente:")
for fila in matriz:
    print(" ".join(f"{num:2}" for num in fila))