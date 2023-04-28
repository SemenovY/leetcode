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
from typing import List, Tuple, Optional


def twosum_with_sort(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """Сортируем исходный массив стандартной функцией"""
    arr.sort()

    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1
    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.


def read_input_with_sort() -> Tuple[List[int], int]:
    """
    Принимаем на вход кол-во двоек, сам массив и число для сравнения.
    :return:
    """
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    """Выводим результат в консоль"""
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input_with_sort()
print_result(twosum_with_sort(arr, target_sum))
