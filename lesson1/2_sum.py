"""
Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.
Во второй строке записано n целых чисел —– очки на фишках
в диапазоне от -105 до 105.
В третьей строке —– загаданное целое число k, -105 ≤ k ≤ 105.
Формат вывода
Нужно вывести два числа в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».
"""
from typing import List, Tuple, Optional, Type


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """
    Через перебор по индексам i and j берем два числа, складываем и сравниваем
    Затем следующие два числа
    Вложенный цикл начинаем с i+1 чтобы исключить i<=j.
    :param arr:
    :param target_sum:
    :return:
    """
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]


def read_input() -> Tuple[List[int], int]:
    """
    Принимаем на вход кол-во двоек, сам массив и число для сравнения.
    :return:
    """
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    """Выводим результат в консоль"""
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
