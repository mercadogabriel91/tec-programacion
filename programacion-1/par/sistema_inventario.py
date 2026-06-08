"""
Sistema de Control de Inventario — ferretería local.

Restricciones del práctico: solo estructuras secuenciales, condicionales y ciclos;
listas paralelas herramientas[] y existencias[]; sin def, clases, diccionarios,
try/except ni estructuras avanzadas.
"""

herramientas = []
existencias = []

salir = False
while not salir:
    print()
    print("========== SISTEMA DE CONTROL DE INVENTARIO ==========")
    print("  1. Carga inicial de herramientas")
    print("  2. Carga de existencias")
    print("  3. Visualización del inventario")
    print("  4. Consulta de stock por herramienta")
    print("  5. Reporte de productos agotados")
    print("  6. Alta de un nuevo producto")
    print("  7. Actualización de stock (venta / ingreso)")
    print("  8. Salir")
    print("======================================================")
    opcion = input("Seleccione una opción (1-8): ").strip()

    if opcion == "1":
        cantidad_raw = input(
            "Cuántas herramientas desea registrar? "
        ).strip()
        cantidad_valida = False
        cantidad_herramientas = 0
        while not cantidad_valida:
            if cantidad_raw == "":
                print("Error: debe ingresar un número entero positivo.")
                cantidad_raw = input(
                    "Cuántas herramientas desea registrar? "
                ).strip()
                continue
            
            solo_digitos = True
            indice_caracter = 0
            
            while indice_caracter < len(cantidad_raw):
                caracter = cantidad_raw[indice_caracter]
                if caracter < "0" or caracter > "9":
                    solo_digitos = False
                    break
                indice_caracter = indice_caracter + 1
                
            if not solo_digitos:
                print("Error: debe ingresar un número entero positivo.")
                cantidad_raw = input(
                    "Cuántas herramientas desea registrar? "
                ).strip()
                continue
            
            valor = 0
            indice_caracter = 0
            
            while indice_caracter < len(cantidad_raw):
                caracter = cantidad_raw[indice_caracter]
                digito = ord(caracter) - ord("0")
                valor = valor * 10 + digito
                indice_caracter = indice_caracter + 1
                
            if valor < 1:
                print("Error: la cantidad debe ser al menos 1.")
                cantidad_raw = input(
                    "Cuántas herramientas desea registrar? "
                ).strip()
                continue
            
            cantidad_herramientas = valor
            cantidad_valida = True

        herramientas = []
        existencias = []
        indice_carga = 0
        while indice_carga < cantidad_herramientas:
            nombre = input(
                "Nombre de la herramienta "
                + str(indice_carga + 1)
                + "/"
                + str(cantidad_herramientas)
                + ": "
            ).strip()
            if nombre == "":
                print("Error: el nombre no puede estar vacío. Intente de nuevo.")
                continue
            es_duplicado = False
            j = 0
            while j < len(herramientas):
                if herramientas[j] == nombre:
                    es_duplicado = True
                    break
                j = j + 1
            if es_duplicado:
                print(
                    "Error: ya existe una herramienta con ese nombre. "
                    "Intentá de nuevo."
                )
                continue
            herramientas.append(nombre)
            indice_carga = indice_carga + 1
        print("Carga inicial de nombres finalizada.")

    elif opcion == "2":
        if len(herramientas) == 0:
            print(
                "Error: debe ejecutar primero la carga inicial de herramientas "
                "(opción 1)."
            )
        else:
            existencias = []
            i = 0
            while i < len(herramientas):
                print(
                    "Existencias para: "
                    + herramientas[i]
                )
                stock_raw = input(
                    "Cantidad de unidades (entero >= 0): "
                ).strip()
                stock_valido = False
                unidades = 0
                while not stock_valido:
                    if stock_raw == "":
                        print(
                            "Error: ingrese un entero mayor o igual que 0."
                        )
                        stock_raw = input(
                            "Cantidad de unidades (entero >= 0): "
                        ).strip()
                        continue
                    solo_digitos_s = True
                    indice_caracter = 0
                    while indice_caracter < len(stock_raw):
                        caracter = stock_raw[indice_caracter]
                        if caracter < "0" or caracter > "9":
                            solo_digitos_s = False
                            break
                        indice_caracter = indice_caracter + 1
                    if not solo_digitos_s:
                        print(
                            "Error: ingrese un entero mayor o igual que 0."
                        )
                        stock_raw = input(
                            "Cantidad de unidades (entero >= 0): "
                        ).strip()
                        continue
                    vu = 0
                    indice_caracter = 0
                    while indice_caracter < len(stock_raw):
                        caracter = stock_raw[indice_caracter]
                        digito = ord(caracter) - ord("0")
                        vu = vu * 10 + digito
                        indice_caracter = indice_caracter + 1
                    unidades = vu
                    stock_valido = True
                existencias.append(unidades)
                i = i + 1
            print("Carga de existencias completada.")

    elif opcion == "3":
        if len(herramientas) == 0:
            print("No hay herramientas cargadas. Use la opción 1 primero.")
        elif len(existencias) != len(herramientas):
            print(
                "Error: falta completar la carga de existencias (opción 2)."
            )
        else:
            print()
            print("--- Inventario actual ---")
            idx = 0
            while idx < len(herramientas):
                print(
                    "  "
                    + herramientas[idx]
                    + " → "
                    + str(existencias[idx])
                    + " unidad(es)"
                )
                idx = idx + 1
            print("-------------------------")

    elif opcion == "4":
        if len(herramientas) == 0:
            print("No hay herramientas en el catálogo. Use la opción 1 primero.")
        elif len(existencias) != len(herramientas):
            print(
                "Error: falta completar la carga de existencias (opción 2)."
            )
        else:
            buscar = input("Nombre de la herramienta a consultar: ").strip()
            encontrado = False
            pos = -1
            t = 0
            while t < len(herramientas):
                if herramientas[t] == buscar:
                    encontrado = True
                    pos = t
                    break
                t = t + 1
            if not encontrado:
                print(
                    "Error: la herramienta no existe en el catálogo."
                )
            else:
                print(
                    "Stock de '"
                    + herramientas[pos]
                    + "': "
                    + str(existencias[pos])
                    + " unidad(es)."
                )

    elif opcion == "5":
        if len(herramientas) == 0:
            print("No hay herramientas cargadas.")
        elif len(existencias) != len(herramientas):
            print(
                "Error: falta completar la carga de existencias (opción 2)."
            )
        else:
            print()
            print("--- Productos agotados (stock = 0) ---")
            hay_agotados = False
            r = 0
            while r < len(herramientas):
                if existencias[r] == 0:
                    print("  - " + herramientas[r])
                    hay_agotados = True
                r = r + 1
            if not hay_agotados:
                print("  (ninguno)")
            print("----------------------------------------")

    elif opcion == "6":
        nombre_nuevo = input("Nombre del nuevo producto: ").strip()
        stock_nuevo_raw = input(
            "Stock inicial (entero >= 0): "
        ).strip()

        error_msg = ""
        if nombre_nuevo == "":
            error_msg = "El nombre no puede estar vacío."
        else:
            dup = False
            d = 0
            while d < len(herramientas):
                if herramientas[d] == nombre_nuevo:
                    dup = True
                    break
                d = d + 1
            if dup:
                error_msg = "Ya existe una herramienta con ese nombre."

        if error_msg == "":
            if stock_nuevo_raw == "":
                error_msg = "El stock debe ser un entero mayor o igual que 0."
            else:
                solo_d = True
                indice_caracter = 0
                while indice_caracter < len(stock_nuevo_raw):
                    caracter = stock_nuevo_raw[indice_caracter]
                    if caracter < "0" or caracter > "9":
                        solo_d = False
                        break
                    indice_caracter = indice_caracter + 1
                if not solo_d:
                    error_msg = (
                        "El stock debe ser un entero mayor o igual que 0."
                    )

        if error_msg != "":
            print("No se pudo dar de alta el producto: " + error_msg)
        else:
            stock_ini = 0
            indice_caracter = 0
            while indice_caracter < len(stock_nuevo_raw):
                caracter = stock_nuevo_raw[indice_caracter]
                digito = ord(caracter) - ord("0")
                stock_ini = stock_ini * 10 + digito
                indice_caracter = indice_caracter + 1
            herramientas.append(nombre_nuevo)
            existencias.append(stock_ini)
            print(
                "Producto agregado: "
                + nombre_nuevo
                + " con "
                + str(stock_ini)
                + " unidad(es)."
            )

    elif opcion == "7":
        if len(herramientas) == 0:
            print("No hay herramientas en el catálogo.")
        elif len(existencias) != len(herramientas):
            print(
                "Error: las listas de herramientas y existencias no están "
                "alineadas. Complete la opción 2 o revise los datos."
            )
        else:
            print("  a) Venta (reduce stock)")
            print("  b) Ingreso de mercadería (aumenta stock)")
            tipo_mov = input("Tipo de movimiento (a/b): ").strip().lower()
            if tipo_mov != "a" and tipo_mov != "b":
                print("Opción no válida.")
            else:
                nom_mov = input(
                    "Nombre de la herramienta: "
                ).strip()
                idx_mov = -1
                m = 0
                while m < len(herramientas):
                    if herramientas[m] == nom_mov:
                        idx_mov = m
                        break
                    m = m + 1
                if idx_mov < 0:
                    print(
                        "Error: la herramienta no existe en el catálogo."
                    )
                elif tipo_mov == "a":
                    cant_raw = input(
                        "Cantidad a vender (entero > 0): "
                    ).strip()
                    cant_ok = False
                    cant_v = 0
                    while not cant_ok:
                        if cant_raw == "":
                            print("Error: ingrese un entero positivo.")
                            cant_raw = input(
                                "Cantidad a vender (entero > 0): "
                            ).strip()
                            continue
                        sd = True
                        indice_caracter = 0
                        while indice_caracter < len(cant_raw):
                            caracter = cant_raw[indice_caracter]
                            if caracter < "0" or caracter > "9":
                                sd = False
                                break
                            indice_caracter = indice_caracter + 1
                        if not sd:
                            print("Error: ingrese un entero positivo.")
                            cant_raw = input(
                                "Cantidad a vender (entero > 0): "
                            ).strip()
                            continue
                        cant_v = 0
                        indice_caracter = 0
                        while indice_caracter < len(cant_raw):
                            caracter = cant_raw[indice_caracter]
                            digito = ord(caracter) - ord("0")
                            cant_v = cant_v * 10 + digito
                            indice_caracter = indice_caracter + 1
                        if cant_v < 1:
                            print("Error: la cantidad debe ser al menos 1.")
                            cant_raw = input(
                                "Cantidad a vender (entero > 0): "
                            ).strip()
                            continue
                        cant_ok = True
                    if cant_v > existencias[idx_mov]:
                        print(
                            "Error: stock insuficiente. Disponible: "
                            + str(existencias[idx_mov])
                            + "."
                        )
                    else:
                        existencias[idx_mov] = existencias[idx_mov] - cant_v
                        print(
                            "Venta registrada. Nuevo stock de '"
                            + herramientas[idx_mov]
                            + "': "
                            + str(existencias[idx_mov])
                            + "."
                        )
                else:
                    cant_in_raw = input(
                        "Cantidad ingresada (entero >= 0): "
                    ).strip()
                    cin_ok = False
                    cant_in = 0
                    while not cin_ok:
                        if cant_in_raw == "":
                            print(
                                "Error: ingrese un entero mayor o igual que 0."
                            )
                            cant_in_raw = input(
                                "Cantidad ingresada (entero >= 0): "
                            ).strip()
                            continue
                        sd2 = True
                        indice_caracter = 0
                        while indice_caracter < len(cant_in_raw):
                            caracter = cant_in_raw[indice_caracter]
                            if caracter < "0" or caracter > "9":
                                sd2 = False
                                break
                            indice_caracter = indice_caracter + 1
                        if not sd2:
                            print(
                                "Error: ingrese un entero mayor o igual que 0."
                            )
                            cant_in_raw = input(
                                "Cantidad ingresada (entero >= 0): "
                            ).strip()
                            continue
                        cant_in = 0
                        indice_caracter = 0
                        while indice_caracter < len(cant_in_raw):
                            caracter = cant_in_raw[indice_caracter]
                            digito = ord(caracter) - ord("0")
                            cant_in = cant_in * 10 + digito
                            indice_caracter = indice_caracter + 1
                        cin_ok = True
                    existencias[idx_mov] = existencias[idx_mov] + cant_in
                    print(
                        "Ingreso registrado. Nuevo stock de '"
                        + herramientas[idx_mov]
                        + "': "
                        + str(existencias[idx_mov])
                        + "."
                    )

    elif opcion == "8":
        print("Fin del sistema. ¡Hasta luego!")
        salir = True

    else:
        print("Opción no válida. Elija un número entre 1 y 8.")
