# Crear el archivo 'my_notes.txt'
archivo_datos = open('my_notes.txt', 'w')  # Abre el archivo en modo escritura

# Escritura del Archivo de Texto
archivo_datos.write("Nombres: Gustavo Rodríguez\n")
archivo_datos.write("Edad: 40 años\n")
archivo_datos.write("Profesión: Ingeniero en TIC\n")
archivo_datos.write("Ciudad de Residencia: Tena\n")
archivo_datos.write("e-mail: ec_garh@hotmail.com\n")
archivo_datos.close()  # Cierra el archivo después de escribir

# Abrir y leer el archivo 'my_notes.txt'
archivo_datos = open('my_notes.txt', 'r')   # Abre el archivo en modo lectura
line = archivo_datos.readline()             # Guarda la información del archivo en la variable "line"
while line:
    print(line.replace("\n", " "))       # Muestra cada línea de información eliminando saltos de línea adicionales
    line = archivo_datos.readline()      #  Lee el contenido del archivo línea por línea

archivo_datos.close()       # Cierra el archivo al finalizar los procesos
