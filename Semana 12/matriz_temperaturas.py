# Matriz 3D de temperaturas diarias en varias ciudades
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            ["Lunes", 28],
            ["Martes", 30],
            ["Miércoles", 31],
            ["Jueves", 29],
            ["Viernes", 32]
        ],
        [   # Semana 2
            ["Lunes", 27],
            ["Martes", 29],
            ["Miércoles", 30],
            ["Jueves", 28],
            ["Viernes", 31]
        ],
        [   # Semana 3
            ["Lunes", 26],
            ["Martes", 8],
            ["Miércoles", 29],
            ["Jueves", 27],
            ["Viernes", 30]
        ],
        [   # Semana 4
            ["Lunes", 28],
            ["Martes", 30],
            ["Miércoles", 31],
            ["Jueves", 29],
            ["Viernes", 32]
        ]
    ],
    [   # Quito
        [   # Semana 1
            ["Lunes", 20],
            ["Martes", 21],
            ["Miércoles", 22],
            ["Jueves", 19],
            ["Viernes", 23]
        ],
        [   # Semana 2
            ["Lunes", 21],
            ["Martes", 22],
            ["Miércoles", 23],
            ["Jueves", 20],
            ["Viernes", 24]
        ],
        [   # Semana 3
            ["Lunes", 19],
            ["Martes", 20],
            ["Miércoles", 21],
            ["Jueves", 18],
            ["Viernes", 22]
        ],
        [   # Semana 4
            ["Lunes", 22],
            ["Martes", 23],
            ["Miércoles", 24],
            ["Jueves", 21],
            ["Viernes", 25]
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            ["Lunes", 18],
            ["Martes", 19],
            ["Miércoles", 20],
            ["Jueves", 17],
            ["Viernes", 21]
        ],
        [   # Semana 2
            ["Lunes", 19],
            ["Martes", 20],
            ["Miércoles", 21],
            ["Jueves", 18],
            ["Viernes", 22]
        ],
        [   # Semana 3
            ["Lunes", 17],
            ["Martes", 18],
            ["Miércoles", 19],
            ["Jueves", 16],
            ["Viernes", 20]
        ],
        [   # Semana 4
            ["Lunes", 20],
            ["Martes", 21],
            ["Miércoles", 22],
            ["Jueves", 19],
            ["Viernes", 23]
        ]
    ],
    [   # Tena
        [   # Semana 1
            ["Lunes", 24],
            ["Martes", 26],
            ["Miércoles", 27],
            ["Jueves", 25],
            ["Viernes", 28]
        ],
        [   # Semana 2
            ["Lunes", 25],
            ["Martes", 27],
            ["Miércoles", 28],
            ["Jueves", 26],
            ["Viernes", 29]
        ],
        [   # Semana 3
            ["Lunes", 23],
            ["Martes", 25],
            ["Miércoles", 26],
            ["Jueves", 24], ["Viernes", 27]
        ],
        [   # Semana 4
            ["Lunes", 26],
            ["Martes", 28],
            ["Miércoles", 29],
            ["Jueves", 27],
            ["Viernes", 30]
        ]
    ]
]

# Mostrar un menú para seleccionar la ciudad
print("Elige una ciudad:")
print("1. Guayaquil")
print("2. Quito")
print("3. Cuenca")
print("4. Tena")

# Obtener la selección del usuario
opcion = int(input("Ingresa el número de la ciudad a consultar: "))

# Validar la entrada y asignar el índice de la ciudad
if opcion == 1:
    indice_ciudad = 0
    ciudad = "Guayaquil"
elif opcion == 2:
    indice_ciudad = 1
    ciudad = "Quito"
elif opcion == 3:
    indice_ciudad = 2
    ciudad = "Cuenca"
elif opcion == 4:
    indice_ciudad = 3
    ciudad = "Tena"
else:
    print("Opción no válida")
    exit()

# Calcular el promedio de temperaturas por semana para la ciudad seleccionada usando un tFOR
print(f"Promedio de temperaturas en {ciudad}:")

for semana in range(4):  # Recorre las semanas
    suma_temperaturas = 0
    for dia in range(5):  # Recorre los días de la semana
        suma_temperaturas += temperaturas[indice_ciudad][semana][dia][1]  # Acceder a la temperatura del día
    promedio = suma_temperaturas / 5
    print(f"Semana {semana + 1}: {promedio:.2f}°C")