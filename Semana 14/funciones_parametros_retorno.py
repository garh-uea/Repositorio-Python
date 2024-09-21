# Función para calcular el descuento
def calcular_descuento(monto, porcentaje_descuento=10):
    descuento = monto * (porcentaje_descuento / 100)
    monto_con_descuento = monto - descuento
    return monto_con_descuento, descuento  # Devuelve el monto del descuento calculado y el descuento obtenido por la compra.


def procesar_cliente():
    while True:
        # Inicializar variables
        total_compra = 0  # Acumula los valores de cada compra para obtener un Total
        total_descuento = 0  # Acumula los montos de descuentos para obtener un Total
        num_productos = 0  # Contador de productos
        print("********************* Papeleria Compu Click *********************\n")
        # Ingresa los datos del cliente
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        # Bucle para ingresar productos
        while True:
            num_productos += 1  # Incrementa el número de productos

            # Ingresar el nombre del producto
            producto = input(f"Ingrese el nombre del producto {num_productos}: ")

            valor_producto = input(f"Ingrese el valor del producto {producto}: ")  # Ingresar el valor del producto
            while not valor_producto.replace('.', '', 1).isdigit() or valor_producto.count(
                    '.') > 1:  # Valida que el valor del producto sea numérico
                print("Por favor, ingrese un valor numérico válido para el precio del producto.")
                valor_producto = input(f"Ingrese el valor del producto {producto}: ")
            valor_producto = float(valor_producto)

            # Preguntar si aplica descuento
            aplica_descuento = input("¿Desea aplicar un 10% de descuento en este producto? (s/n): ").lower()

            # Calcular el monto con o sin descuento
            if aplica_descuento == 's':
                monto_con_descuento, descuento = calcular_descuento(
                    valor_producto)  # Llama a la función para realizar el respectivo descuento y devuelve el monto a pagar con descuento y el descuento obtenido
            else:
                monto_con_descuento, descuento = calcular_descuento(valor_producto, 0)

            # Acumular los valores
            total_compra += monto_con_descuento
            total_descuento += descuento

            # Pregunta si desea seguir agregando más productos (mínimo 2 productos)
            if num_productos >= 2:
                continuar = input("¿Desea ingresar otro producto para este cliente? (s/n): ").lower()
                if continuar != 's':
                    break

        # Mostrar el total de la compra y el total del descuento aplicado
        print(f"\nNombre del Cliente: {nombre_cliente}")
        print(f"Total de la compra: ${total_compra:.2f}")
        print(f"Total del descuento aplicado: ${total_descuento:.2f}\n")

        # Pregunta si desea procesar los datos de otro cliente
        nuevo_cliente = input("¿Desea ingresar los datos de un nuevo cliente? (s/n): ").lower()
        if nuevo_cliente != 's':
            print("Fin del programa.")
            break


# Ejecutar el programa
procesar_cliente()  # Llama a la función principal para iniciar la ejecución del programa.