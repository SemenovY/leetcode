"""
Получаем на входе два числа в двоичной системе счисления
Необходимо вывести их сумму, также в двоичной системе
Решение должно работать за O(N),
где N –— количество разрядов максимального числа на входе
Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке
Длина каждого числа не превосходит 10 000 символов
Формат вывода
Одно число в двоичной системе счисления.
"""
from typing import Tuple


def get_sum(first_number, second_number):
    """
    Получаем на вход два двоичных числа
    Заносим в списки
    Дополняем нулями
    Прогоняем по списку, сравниваем с условиями и создаем новый список
    В каждой проверке обновляем значение value
    В конце итерируемого списка если флаг переполнен, добавляем 1.
    :param first_number:
    :param second_number:
    :return:
    """
    # получаем числа и переворачиваем для удобства подсчета
    first_number = first_number[::-1]
    second_number = second_number[::-1]
    # дополнить нулями
    size = max(len(first_number), len(second_number))
    first_number += [0]*(size - len(first_number))
    second_number += [0]*(size - len(second_number))
    # переменные
    result = []
    overflow = 0
    # код
    for i in zip(first_number, second_number):
        value = i[0] + i[1] + overflow
    #  другой вариант решения
    #   overflow = value // 2
    #   result.append(value%2)

        if value == 0:
            result.append(0)
            overflow = 0
        if value == 1:
            result.append(1)
            overflow = 0
        if value == 2:
            result.append(0)
            overflow = 1
        if value == 3:
            result.append(1)
            overflow = 1
    # если флаг переполнения установлен - добавить бит в начало нового числа
    if overflow == 1:
        result.append(1)
    result = map(int, result[::-1])
    result = " ".join(list(map(str, result)))
    result = str(result.replace(' ', ''))
    return result


def read_input():
    """
    Формат ввода
    Два числа в двоичной системе счисления, каждое на отдельной строке.
    Длина каждого числа не превосходит 10 000 символов.
    :return:
    """
    # получить бинарное число в виде массива чисел (бит)
    first_number = [*map(int, input("Введите первое число в 2ой системе: "))]
    second_number = [*map(int, input("Введите второе число в 2ой системе: "))]
    return first_number, second_number


first_number, second_number = read_input()
# Формат вывода
# Одно число в двоичной системе счисления.
print(get_sum(first_number, second_number))
