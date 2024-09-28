# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "Nombres": "Gustavo Adolfo",
    "Apellidos": "Rodríguez Holguin",
    "Edad": 40,
    "Ciudad de residencia": "Tena",
    "Estado Civil": "Casado",
    "Nivel de Educación": "Secundaria",
    "e-mail": "ec_garh@hotmail.com"
}

# Imprimir el diccionario Inicial
print("************************* Datos del Usuario*************************\n", informacion_personal)

# Acceder y modificar el valor de la clave "ciudad de residencia"
nueva_ciudad = input("Ingrese la nueva Ciudad de Residencia: ")
informacion_personal["Ciudad de residencia"] = nueva_ciudad

# Agregar una nueva clave-valor al diccionario que represente la Profesión de la persona
profesion = input("Ingrese la Profesión del Usuario: ")
informacion_personal["Profesion"] = profesion

# Verificar si la clave "Teléfono" existe y agregarla si no existe
if "Teléfono" not in informacion_personal:
    telefono = input("Ingrese número de teléfono del Usuario: ")
    informacion_personal["Teléfono"] = telefono

# Eliminar la clave "Edad" del diccionario
del informacion_personal["Edad"]

# Imprimir el diccionario resultante
print("\n**********************Datos Finales del Usuario:**********************\n", informacion_personal)
