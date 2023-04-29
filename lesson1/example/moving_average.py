"""
Метод скользящего среднего
с применением метода двух указателей
В алгоритме есть два указателя:
они задают начало и конец рассматриваемого интервала.
Чтобы пересчитать среднее арифметическое:
сначала изменяем его исходя из тех значений, на которые ссылаются указатели,
а потом эти указатели смещаем.
"""
from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    """
    Создаем пустой массив
    добавляем в него значение первой итерации
    затем через цикл
    меняем значение первой итерации отнимая первый индекс
    и добавляя последний.

    :param arr:
    :param window_size:
    :return:
    """
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)
    for i in range(0, len(arr) - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    """
    Получаем данные из ввода.
    :return:
    """
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))