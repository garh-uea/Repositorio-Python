import random

# Solicitamos al usuario que ingrese el tamaño de las filas para la matriz
filas = int(input("Ingresa el tamaño de filas para la matriz: "))

# Solicitamos al usuario que ingrese el tamaño de las columnas para la matriz
columnas = int(input("Ingresa el tamaño de columnas para la matriz: "))

# Inicializamos la matriz como una lista vacía
matriz = []

# Generamos la matriz (filas)x(columnas) con valores aleatorios entre 1 y 99
for i in range(filas):
    fila = []  # Creamos una lista vacia para la fila actual
    for j in range(columnas):
        num_generado = random.randint(1, 99)
        fila.append(num_generado)  # Añadimos el número generado a la fila actual
    matriz.append(fila)  # Añadimos la fila completa a la matriz

# Mostramos la matriz generada
print("Matriz generada automáticamente:")
for i in matriz:
    print(" ".join(f"{num:2}" for num in i))

# Solicitamos al usuario que ingrese el valor que desea buscar en la matriz generada
valor_buscado = int(input("Ingresa el valor que deseas buscar en la matriz: "))

# Inicializamos una variable para verificar si encontramos el valor
encontrado = False

# Recorremos la matriz para buscar el valor
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == valor_buscado:
            print(f"Valor {valor_buscado} encontrado en la posición ({i}, {j})")
            encontrado = True
            break
    if encontrado:
        break

# Si el valor no se encontró, mostramos un mensaje
if not encontrado:
    print(f"Valor {valor_buscado} no se encuentra en la matriz.")
