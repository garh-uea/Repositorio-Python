import random

# Función principal para ejecutar el programa
def main():
    # Ingresar el número de ciudades para su Registro
    print("********************* Rastreo de temperaturas por Ciudades *********************\n")
    cant_ciudad = int(input("Ingrese el número de ciudades: "))
    ciudades = ingresar_nombres_ciudades(cant_ciudad)   # Ejecuta la función para el ingreso de las ciudades y se almacenan en la variable "ciudades"

    # Ingresar el número de semanas para el registro diario de temperaturas
    semanas = int(input("\nIngrese el número de semanas para su Registro: "))

    temperaturas = generar_matriz_temp(cant_ciudad, semanas)    # Ejecuta la función para el ingreso de las temperaturas y se almacenan en la variable "temperaturas"

    calcular_y_mostrar_promedios(temperaturas, ciudades)        # Función para calcular y mostrar el promedio de temperaturas, recibiendo los parámetros necesarios: temperaturas y ciudades a procesar

    op = input("\n¿Desea visualizar el registro de temperaturas por día, semanas y por ciudad? (s/n): ").lower()
    if op == 's':
        mostrar_matriz_temp(cant_ciudad, ciudades, semanas, temperaturas)

# Función para ingresar los nombres de las ciudades
def ingresar_nombres_ciudades(cant_ciudad):
    ciudades = []
    for i in range(cant_ciudad):  # Recorre la matriz de acuerdo a la cantidad de ciudades ingresadas
        ciudad = input(f"Ingrese el nombre de la ciudad {i + 1}: ")
        ciudades.append(ciudad)  # Agrega cada ciudad a la matriz
    return ciudades  # Retorna la lista con todas las ciudades ingresadas


# Función para generar la matriz de temperaturas
def generar_matriz_temp(cant_ciudad, semanas):
    temperaturas = []
    for i in range(cant_ciudad):  # Recorre el primer FOR el número de veces de las ciudades ingresadas
        ciudad_temperaturas = []
        for j in range(semanas):  # Recorre el segundo FOR el número de semanas ingresadas
            semana_temperaturas = []
            for k in range(7):  # Recorre el tercer FOR el número de días de la semana Lunes a Domingo (7)
                dia_temperatura = [f"Día {k + 1}", random.randint(12, 38)]  # Temperaturas aleatorias entre 12 a 38 grados
                semana_temperaturas.append(dia_temperatura)  # Agrega las temperaturas a cada semana del registro
            ciudad_temperaturas.append(semana_temperaturas)  # Agrega las semanas con su registro de temperaturas a cada ciudad
        temperaturas.append(ciudad_temperaturas)
    return temperaturas  # Retorna la matriz con todas las temperaturas generadas en cada día y por cada semana


# Función para calcular y mostrar el promedio de temperaturas
def calcular_y_mostrar_promedios(temperaturas, ciudades):
    indice_ciudad = 0  # Variable para llevar el control del índice de las ciudades.
    for ciudad_temperaturas in temperaturas:  # Bucle para iterar sobre las temperaturas de cada ciudad.
        print(f"\nPromedio de temperaturas en {ciudades[indice_ciudad]}:")

        indice_semana = 0  # Variable para llevar el control del índice de las semanas.
        for semana_temperaturas in ciudad_temperaturas:  # Bucle para iterar sobre las temperaturas de cada semana.
            suma_temperaturas = 0
            for dia_temperatura in semana_temperaturas:  # Bucle para sumar las temperaturas de los días de la semana.
                suma_temperaturas += dia_temperatura[1]
            promedio = suma_temperaturas / len(semana_temperaturas)
            print(f"Semana {indice_semana + 1}: {promedio:.2f}°C")  # Imprime el promedio de temperaturas para cada semana, con 2 dígitos después del punto decimal.

            indice_semana += 1

        indice_ciudad += 1

# Función Opcional para mostrar la matriz 3D de las temperaturas de las ciudades registradas por días y por cada semana
def mostrar_matriz_temp(cant_ciudad, ciudades, semanas, temperaturas):
    for i in range(cant_ciudad):  # Recorre el primer FOR el número de veces de las ciudades ingresadas
        print(f"Ciudad: {ciudades[i]}")
        for j in range(semanas):  # Recorre el segundo FOR el número de semanas ingresadas
            print(f" Semana {j + 1}")
            for k in range(7):  # Recorre el tercer FOR el número de días de la semana Lunes a Domingo (7)
                print(f"  Día {k + 1} - Temperatura: {temperaturas[i][j][k][1]}°C")     # Muestra el día y la temperatura de la semana y la ciudad correspondiente
        print("\n")


# Ejecutar el programa
main()  # Llama a la función principal para iniciar la ejecución del programa.