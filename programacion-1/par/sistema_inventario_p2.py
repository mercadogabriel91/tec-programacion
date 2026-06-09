# # LINK AL VIDEO: https://youtu.be/KEiaIY1ihAU
"""
Sistema de Control de Inventario — Parcial 2 (Programación 1).

Estructura permitida: listas de diccionarios inventario[],
funciones def, condicionales, ciclos y try/except.
Sin variables globales, clases ni estructuras no autorizadas.
"""


def normalizar_nombre(nombre):
    """Compara nombres ignorando mayúsculas y espacios extremos."""
    return nombre.strip().lower()


def buscar_indice(inventario, nombre_a_buscar):
    """Te da el índice de la herramienta o -1 si no existe."""
    nombre_normalizado = normalizar_nombre(nombre_a_buscar)
    indice = 0

    while indice < len(inventario):
        nombre_item = inventario[indice]["herramienta"]
        if normalizar_nombre(nombre_item) == nombre_normalizado:
            return indice
        indice = indice + 1

    return -1


def existe_herramienta(inventario, nombre):
    return buscar_indice(inventario, nombre) >= 0


def pedir_entero_positivo(mensaje):
    """Pide un entero estrictamente mayor que cero."""
    while True:
        try:
            texto = input(mensaje).strip()
            valor = int(texto)
            if valor <= 0:
                raise ValueError("Debe ingresar un entero mayor que cero.")
            return valor
        except ValueError as error:
            if str(error) == "Debe ingresar un entero mayor que cero.":
                print(f"Error: {error}")
            else:
                print("Error: debe ingresar un número entero válido.")


def pedir_entero_no_negativo(mensaje):
    """Pide un entero mayor o igual que cero."""
    while True:
        try:
            texto = input(mensaje).strip()
            valor = int(texto)
            if valor < 0:
                raise ValueError("El stock no puede ser negativo.")
            return valor
        except ValueError as error:
            if str(error) == "El stock no puede ser negativo.":
                print(f"Error: {error}")
            else:
                print("Error: debe ingresar un número entero válido.")


def mostrar_menu():
    print()
    print("========== SISTEMA DE CONTROL DE INVENTARIO ==========")
    print("  1. Carga de herramientas con existencias iniciales")
    print("  2. Visualización de inventario")
    print("  3. Consulta de stock")
    print("  4. Reporte de agotados")
    print("  5. Alta de nuevo producto")
    print("  6. Actualización de stock (venta / ingreso)")
    print("  7. Salir")
    print("======================================================")


def cargar_herramientas(inventario):
    if len(inventario) > 0:
        print(
            "El inventario ya contiene herramientas. "
            "Use la opción 5 para dar de alta un nuevo producto."
        )
        return

    cantidad = pedir_entero_positivo("Cuántas herramientas desea cargar? ")
    cargadas = 0

    while cargadas < cantidad:
        try:
            nombre = input(
                f"Nombre de la herramienta ({cargadas + 1}/{cantidad}): "
            ).strip()

            if nombre == "":
                raise ValueError("El nombre no puede estar vacío.")

            if existe_herramienta(inventario, nombre):
                raise ValueError("Ya existe una herramienta con ese nombre.")

            stock = pedir_entero_no_negativo("Stock inicial (entero >= 0): ")

            item = {"herramienta": nombre, "cantidad": stock}
            inventario.append(item)
            cargadas = cargadas + 1

        except ValueError as error:
            print(f"Error: {error}")


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    print()
    print("--- Inventario actual ---")
    indice = 0
    while indice < len(inventario):
        herramienta = inventario[indice]["herramienta"]
        cantidad = inventario[indice]["cantidad"]
        print(f"  {herramienta} → {cantidad} unidad(es)")
        indice = indice + 1
    print("-------------------------")


def consultar_stock(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    nombre = input("Nombre de la herramienta a consultar: ").strip()
    indice = buscar_indice(inventario, nombre)

    if indice < 0:
        print("La herramienta no existe en el catálogo.")
        return

    herramienta = inventario[indice]["herramienta"]
    cantidad = inventario[indice]["cantidad"]
    print(f"Stock de '{herramienta}': {cantidad} unidad(es).")


def reporte_agotados(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    print()
    print("--- Productos agotados (stock = 0) ---")
    hay_agotados = False
    indice = 0

    while indice < len(inventario):
        if inventario[indice]["cantidad"] == 0:
            print(f"  - {inventario[indice]['herramienta']}")
            hay_agotados = True
        indice = indice + 1

    if not hay_agotados:
        print("  (ninguno)")
    print("--------------------------------------")


def alta_producto(inventario):
    try:
        nombre = input("Nombre del nuevo producto: ").strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        if existe_herramienta(inventario, nombre):
            raise ValueError("Ya existe una herramienta con ese nombre.")

        stock = pedir_entero_no_negativo("Stock inicial (entero >= 0): ")

        item = {"herramienta": nombre, "cantidad": stock}
        inventario.append(item)
        print(
            f"Producto agregado: {nombre} con {stock} unidad(es)."
        )

    except ValueError as error:
        print(f"No se pudo dar de alta el producto: {error}")


def actualizar_stock(inventario):
    if len(inventario) == 0:
        print(
            "No hay herramientas cargadas. "
            "Debe registrar al menos una herramienta antes de operar stock."
        )
        return

    print("  a) Venta (reduce stock)")
    print("  b) Ingreso de mercadería (aumenta stock)")
    tipo_movimiento = input("Tipo de movimiento (a/b): ").strip().lower()

    if tipo_movimiento != "a" and tipo_movimiento != "b":
        print("Opción no válida.")
        return

    nombre = input("Nombre de la herramienta: ").strip()
    indice = buscar_indice(inventario, nombre)

    if indice < 0:
        print("La herramienta no existe en el catálogo.")
        return

    try:
        if tipo_movimiento == "a":
            cantidad = pedir_entero_positivo("Cantidad a vender (entero > 0): ")
            stock_actual = inventario[indice]["cantidad"]

            if cantidad > stock_actual:
                raise ValueError(
                    f"Stock insuficiente. Disponible: {stock_actual}."
                )

            inventario[indice]["cantidad"] = stock_actual - cantidad
            herramienta = inventario[indice]["herramienta"]
            nuevo_stock = inventario[indice]["cantidad"]
            print(
                f"Venta registrada. Nuevo stock de '{herramienta}': {nuevo_stock}."
            )
        else:
            cantidad = pedir_entero_positivo(
                "Cantidad ingresada (entero > 0): "
            )
            stock_actual = inventario[indice]["cantidad"]
            inventario[indice]["cantidad"] = stock_actual + cantidad
            herramienta = inventario[indice]["herramienta"]
            nuevo_stock = inventario[indice]["cantidad"]
            print(
                f"Ingreso registrado. Nuevo stock de '{herramienta}': {nuevo_stock}."
            )

    except ValueError as error:
        print(f"Error: {error}")


def main():
    inventario = []
    opcion = 0

    while opcion != 7:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-7): ").strip())
            if opcion < 1 or opcion > 7:
                raise ValueError("Opción fuera de rango.")
        except ValueError:
            print("Error: ingrese un número entero entre 1 y 7.")
            opcion = 0
            continue

        if opcion == 1:
            cargar_herramientas(inventario)
        elif opcion == 2:
            mostrar_inventario(inventario)
        elif opcion == 3:
            consultar_stock(inventario)
        elif opcion == 4:
            reporte_agotados(inventario)
        elif opcion == 5:
            alta_producto(inventario)
        elif opcion == 6:
            actualizar_stock(inventario)
        elif opcion == 7:
            print("Saliendo del sistema... gracias!")


if __name__ == "__main__":
    main()
