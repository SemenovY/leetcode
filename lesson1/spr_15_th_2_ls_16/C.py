"""
Дана матрица.
Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево,
вправо, вверх или вниз.
Диагональные элементы соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0.
А для (2, 1) –— 1, 2, 7, 7.
"""


def get_neighbours(matrix, row, column):
    """
    В цикле сначала задаем позицию в столбце сверху и снизу от сущности
    Затем проверяем начальный и конечный индексы, на исключение
    Добавляем в словарь если есть что
    Опять перебор, но уже слева справа
    И так же добавляем в словарь.
    :param matrix:
    :param row:
    :param column:
    :param n:
    :param m:
    :return: result
    """

    result = []

    for col_m in (column-1, column+1):  # Координаты элемента по столбцам
        try:
            if col_m >= 0:
                result.append(matrix[row][col_m])  # left, right
        except Exception:
            pass

    for row_n in (row-1, row+1):  # Координаты элемента по строкам
        try:
            if row_n >= 0:
                result.append(matrix[row_n][column])  # up, down
        except Exception:
            pass

    return sorted(result)


def read_input():
    """
    Формат ввода
    В первой строке задано n — количество строк матрицы.
    Во второй — количество столбцов m. Числа m и n не превосходят 1000.
    В следующих n строках задана матрица.
    Элементы матрицы — целые числа, по модулю не превосходящие 1000.
    В последних двух строках записаны координаты элемента,
    соседей которого нужно найти. Индексация начинается с нуля.
    Формат вывода
    Напечатайте нужные числа в возрастающем порядке через пробел.
    """
    n = int(input())  # rows
    m = int(input())  # columns
    matrix = []
    for i in range(n):  # from matrix to list
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())  # Координаты элемента, строка
    column = int(input())  # Координаты элемента, столбец
    return matrix, row, column


matrix, row, column = read_input()

print(" ".join(map(str, get_neighbours(matrix, row, column))))
