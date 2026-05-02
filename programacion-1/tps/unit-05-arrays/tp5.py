from typing import List, Optional
import random

# ** COMO USAR **
# Simplemente des-comentar el llamado a la función que se quiera probar
# al pie del archivo y ejecutar main.py

# ====================================================================
# Ejercicio 1: Lista con notas de 10 estudiantes: mostrar lista, promedio, máximo y mínimo.
# ====================================================================
def ejercicio_1():
    grades: List[float] = [7.5, 8.0, 6.0, 9.5, 4.0, 10.0, 5.5, 8.5, 7.0, 6.5]

    print("Notas de los 10 estudiantes:\n")
    for i in range(len(grades)):
        print(f"  Estudiante {i + 1}: {grades[i]}")

    total_sum: float = 0.0
    for n in grades:
        total_sum += n
    average: float = total_sum / len(grades)

    highest_grade: float = grades[0]
    lowest_grade: float = grades[0]
    for n in grades:
        if n > highest_grade:
            highest_grade = n
        if n < lowest_grade:
            lowest_grade = n

    print(f"\nPromedio: {average}")
    print(f"Nota más alta: {highest_grade}")
    print(f"Nota más baja: {lowest_grade}\n")

    return 0
    # Fin


# ====================================================================
# Ejercicio 2: Cargar 5 productos; mostrar ordenados con sorted(); eliminar uno pedido al usuario.
# ====================================================================
def ejercicio_2():
    products: List[str] = []

    print("Ingrese el nombre de 5 productos:\n")
    for i in range(5):
        name: str = input(f"Producto {i + 1}/5: ")
        products.append(name.strip())

    alphabetically_sorted: List[str] = sorted(products)
    print("\nLista ordenada alfabéticamente (sorted):\n")
    for p in alphabetically_sorted:
        print(f"  - {p}")

    to_remove: str = input("\n¿Qué producto desea elminar? ").strip()
    updated_list: List[str] = []
    removed_once: bool = False
    for p in products:
        if p == to_remove and not removed_once:
            removed_once = True
            continue
        updated_list.append(p)

    products = updated_list
    if removed_once:
        print("\nLista actualizada:\n")
        for p in products:
            print(f"  - {p}")
    else:
        print("\nEse producto no estaba en la lista (no se eliminó nada).\n")
        for p in products:
            print(f"  - {p}")

    print()
    return 0
    # Fin


# ====================================================================
# Ejercicio 3: 15 enteros al azar entre 1 y 100; listas pares e impares y cantidades.
# ====================================================================
def ejercicio_3():
    numbers: List[int] = []
    for _ in range(15):
        numbers.append(random.randint(1, 100))

    evens: List[int] = []
    odds: List[int] = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    print("Números generados:\n")
    for n in numbers:
        print(f"  {n}")

    print("\nPares:\n")
    for n in evens:
        print(f"  {n}")
    print(f"\nCantidad de pares: {len(evens)}")

    print("\nImpares:\n")
    for n in odds:
        print(f"  {n}")
    print(f"\nCantidad de impares: {len(odds)}\n")

    return 0
    # Fin


# ====================================================================
# Ejercicio 4: Lista con valores repetidos; nueva lista sin repetidos.
# ====================================================================
def ejercicio_4():
    original: List[int] = [1, 2, 2, 3, 4, 4, 5, 1, 3]
    unique_values: List[int] = []

    for x in original:
        already_present: bool = False
        for y in unique_values:
            if y == x:
                already_present = True
                break
        if not already_present:
            unique_values.append(x)

    print("Lista original:\n")
    for x in original:
        print(f"  {x}")

    print("\nLista sin elementos repetidos:\n")
    for x in unique_values:
        print(f"  {x}")
    print()

    return 0
    # Fin


# ====================================================================
# Ejercicio 5: 8 estudiantes; preguntar si agrega o elimina; mostrar lista final.
# ====================================================================
def ejercicio_5():
    students: List[str] = [
        "Ana",
        "Bruno",
        "Carla",
        "Diego",
        "Sofi",
        "Facundo",
        "Sol",
        "Hugo",
    ]

    print("Estudiantes presentes (inicial):\n")
    for e in students:
        print(f"  - {e}")

    choice: str = input(
        '\n¿Desea agregar un estudiante (a) o eliminar uno existente (e)? '
    ).strip().lower()

    if choice == "a":
        new_name: str = input("Nombre del nuevo estudiante: ").strip()
        if new_name:
            students.append(new_name)
    elif choice == "e":
        name_to_remove: str = input("Nombre del estudiante a eliminar: ").strip()
        updated_students: List[str] = []
        did_remove: bool = False
        for e in students:
            if e == name_to_remove and not did_remove:
                did_remove = True
                continue
            updated_students.append(e)
        students = updated_students
        if not did_remove:
            print("Ese nombre no estaba en la lista.")
    else:
        print("Opción no reconocida; la lista no se modfica.")

    print("\nLista final:\n")
    for e in students:
        print(f"  - {e}")
    print()

    return 0
    # Fin


# ====================================================================
# Ejercicio 6: 7 números; rotar una posición a la derecha (el último pasa al primero).
# ====================================================================
def ejercicio_6():
    numbers: List[int] = [10, 20, 30, 40, 50, 60, 70]

    print("Lista original:\n")
    for n in numbers:
        print(f"  {n}")

    if len(numbers) == 0:
        print("\nLa lista está vacía.\n")
        return 0

    rotated: List[int] = []
    rotated.append(numbers[len(numbers) - 1])
    for i in range(len(numbers) - 1):
        rotated.append(numbers[i])

    print("\nLista rotada a la derecha:\n")
    for n in rotated:
        print(f"  {n}")
    print()

    return 0
    # Fin


# ====================================================================
# Ejercicio 7: Matriz 7x2 (mín/máx por día); promedios; día de mayor amplitud térmica.
# ====================================================================
def ejercicio_7():
    weekday_names: List[str] = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo",
    ]
    temperatures: List[List[float]] = []

    print("Ingrese temperatura mínima y máxima para cada día de la semana:\n")
    for i in range(7):
        min_temp = float(input(f"{weekday_names[i]} — mínima: "))
        max_temp = float(input(f"{weekday_names[i]} — máxima: "))
        temperatures.append([min_temp, max_temp])

    sum_mins: float = 0.0
    sum_maxs: float = 0.0
    for row in temperatures:
        sum_mins += row[0]
        sum_maxs += row[1]

    avg_min: float = sum_mins / len(temperatures)
    avg_max: float = sum_maxs / len(temperatures)

    max_amplitude_day_index: int = 0
    max_amplitude: float = temperatures[0][1] - temperatures[0][0]
    for i in range(len(temperatures)):
        amplitude: float = temperatures[i][1] - temperatures[i][0]
        if amplitude > max_amplitude:
            max_amplitude = amplitude
            max_amplitude_day_index = i

    print(f"\nPromedio de mínimas: {avg_min}")
    print(f"Promedio de máximas: {avg_max}")
    print(
        f"Mayor amplitud térmica: {max_amplitude} ({weekday_names[max_amplitude_day_index]})\n"
    )

    return 0
    # Fin


# ====================================================================
# Ejercicio 8: Matriz 5x3 notas; promedio por estudiante y por materia.
# ====================================================================
def ejercicio_8():
    subject_names: List[str] = ["Materia A", "Materia B", "Materia C"]
    grades_matrix: List[List[float]] = []

    print("Ingrese las 3 notas de cada uno de los 5 estudiantes:\n")
    for student_idx in range(5):
        row: List[float] = []
        for subject_idx in range(3):
            grade = float(
                input(f"Estudiante {student_idx + 1}, {subject_names[subject_idx]}: ")
            )
            row.append(grade)
        grades_matrix.append(row)

    print("\nPromedio por estudiante:\n")
    for student_idx in range(5):
        row_sum: float = 0.0
        for subject_idx in range(3):
            row_sum += grades_matrix[student_idx][subject_idx]
        student_avg: float = row_sum / 3.0
        print(f"  Estudiante {student_idx + 1}: {student_avg}")

    print("\nPromedio por materia:\n")
    for subject_idx in range(3):
        col_sum: float = 0.0
        for student_idx in range(5):
            col_sum += grades_matrix[student_idx][subject_idx]
        subject_avg: float = col_sum / 5.0
        print(f"  {subject_names[subject_idx]}: {subject_avg}")
    print()

    return 0
    # Fin


# ====================================================================
# Ejercicio 9: Ta-Te-Ti 3x3 con '-' ; dos jugadores X y O; mostrar tablero tras cada jugada.
# ====================================================================
def ejercicio_9():
    def board_full(board: List[List[str]]) -> bool:
        for row in board:
            for cell in row:
                if cell == "-":
                    return False
        return True

    def player_wins(board: List[List[str]], symbol: str) -> bool:
        for i in range(3):
            if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
                return True
            if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
                return True
        if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
            return True
        if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
            return True
        return False

    board: List[List[str]] = []
    for _ in range(3):
        empty_row: List[str] = ["-", "-", "-"]
        board.append(empty_row)

    symbols: List[str] = ["X", "O"]
    turn_index: int = 0

    print("Ta-Te-Ti. Jugador 1 = X, Jugador 2 = O. Filas y columnas de 0 a 2.\n")

    while True:
        print("Tablero:\n")
        for row in board:
            line: str = ""
            for cell in row:
                line += f" {cell} "
            print(line)

        if board_full(board):
            print("\nEmpate.\n")
            break

        player_number: int = (turn_index % 2) + 1
        current_symbol: str = symbols[turn_index % 2]
        print(f"\nTurno jugador {player_number} ({current_symbol})")

        row_idx = int(input("Fila (0-2): "))
        col_idx = int(input("Columna (0-2): "))
        if row_idx < 0 or row_idx > 2 or col_idx < 0 or col_idx > 2:
            print("Posición fuera de rango.\n")
            continue
        if board[row_idx][col_idx] != "-":
            print("Casilla ocupada.\n")
            continue

        board[row_idx][col_idx] = current_symbol

        if player_wins(board, current_symbol):
            print("\nTablero final:\n")
            for row in board:
                line = ""
                for cell in row:
                    line += f" {cell} "
                print(line)
            print(f"\nGanó el jugador {player_number} ({current_symbol}).\n")
            break

        turn_index += 1

    return 0
    # Fin


# ====================================================================
# Ejercicio 10: Matriz 4x7 ventas; total por producto; día con más ventas; producto más vendido.
# ====================================================================
def ejercicio_10():
    sales: List[List[int]] = []
    random.seed()
    for product_idx in range(4):
        row: List[int] = []
        for day_idx in range(7):
            row.append(random.randint(0, 50))
        sales.append(row)

    print("Matriz de ventas (4 producto × 7 días), valores generados al azar:\n")
    for product_idx in range(4):
        print(f"  Producto {product_idx + 1}: ", end="")
        for day_idx in range(7):
            print(f"{sales[product_idx][day_idx]:3d} ", end="")
        print()

    print("\nTotal vendido por cada producto:\n")
    totals_by_product: List[int] = []
    for product_idx in range(4):
        product_total: int = 0
        for day_idx in range(7):
            product_total += sales[product_idx][day_idx]
        totals_by_product.append(product_total)
        print(f"  Producto {product_idx + 1}: {product_total}")

    totals_by_day: List[int] = []
    for day_idx in range(7):
        day_sum: int = 0
        for product_idx in range(4):
            day_sum += sales[product_idx][day_idx]
        totals_by_day.append(day_sum)

    best_sales_day_index: int = 0
    max_daily_total: int = totals_by_day[0]
    for day_idx in range(1, 7):
        if totals_by_day[day_idx] > max_daily_total:
            max_daily_total = totals_by_day[day_idx]
            best_sales_day_index = day_idx

    print(f"\nDía con mayores ventas totales: día {best_sales_day_index + 1} (total {max_daily_total})")

    best_product_index: int = 0
    max_product_total: int = totals_by_product[0]
    for product_idx in range(1, 4):
        if totals_by_product[product_idx] > max_product_total:
            max_product_total = totals_by_product[product_idx]
            best_product_index = product_idx

    print(f"Producto más vendido en la semana: producto {best_product_index + 1} (total {max_product_total})\n")

    return 0
    # Fin


# ====================================================================
# Ejercicio 11: 10 nombres; buscar uno; indicar si está y la posición.
# ====================================================================
def ejercicio_11():
    students: List[str] = [
        "Lucia",
        "Marcos",
        "Nadia",
        "Oscar",
        "Paula",
        "Rodrigo",
        "Sofia",
        "Tomas",
        "Rocio",
        "Victor",
    ]

    print("Lista de estudiantes:\n")
    for i in range(len(students)):
        print(f"  {i + 1}. {students[i]}")

    name_to_find: str = input("\nNombre a buscar: ").strip()
    found_index: Optional[int] = None
    for i in range(len(students)):
        if students[i] == name_to_find:
            found_index = i
            break

    if found_index is not None:
        print(f"\nEl nombre está en la lista, posición (índice 0): {found_index}, posición humana: {found_index + 1}\n")
    else:
        print("\nEl nombre no está en la lista.\n")

    return 0
    # Fin


# ====================================================================
# Ejercicio 12: 8 enteros; lista original; orden creciente y decreciente con sorted y reverse.
# ====================================================================
def ejercicio_12():
    numbers: List[int] = []

    print("Ingrese 8 números enteros:\n")
    for i in range(8):
        numbers.append(int(input(f"Numero {i + 1}/8: ")))

    print("\nLista original:\n")
    for n in numbers:
        print(f"  {n}")

    ascending: List[int] = sorted(numbers)
    print("\nOrdenada de menor a mayor (sorted):\n")
    for n in ascending:
        print(f"  {n}")

    descending: List[int] = sorted(numbers, reverse=True)
    print("\nOrdenada de mayor a menor (sorted(..., reverse=True)):\n")
    for n in descending:
        print(f"  {n}")
    print()

    return 0
    # Fin


# ====================================================================
# Ejercicio 13: Puntajes del juego; máximo y mínimo; ranking; posición del 990.
# ====================================================================
def ejercicio_13():
    scores: List[int] = [450, 1200, 875, 990, 300, 1500, 640]

    max_score: int = scores[0]
    min_score: int = scores[0]
    for p in scores:
        if p > max_score:
            max_score = p
        if p < min_score:
            min_score = p

    ranking: List[int] = sorted(scores, reverse=True)

    print("Puntajes:\n")
    for p in scores:
        print(f"  {p}")

    print(f"\nPuntaje más alto: {max_score}")
    print(f"Puntaje más bajo: {min_score}")

    print("\nRanking (de mayor a menor):\n")
    rank_position: int = 1
    for p in ranking:
        print(f"  {rank_position}. {p}")
        rank_position += 1

    ranking_place: Optional[int] = None
    target_score: int = 990
    for i in range(len(ranking)):
        if ranking[i] == target_score:
            ranking_place = i + 1
            break

    if ranking_place is not None:
        print(f"\nEl puntaje {target_score} está en el lugar {ranking_place} del ranking.\n")
    else:
        print(f"\nEl puntaje {target_score} no aparece en el ranking.\n")

    return 0
    # Fin


# Repository:
# https://github.com/mercadogabriel91/tec-programacion
# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
# exercicio_6()
# ejercicio_7()
# ejercicio_8()
# ejercicio_9()
# ejercicio_10()
# ejercicio_11()
# ejercicio_12()
# ejercicio_13()
