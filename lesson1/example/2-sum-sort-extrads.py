"""
Второй вариант оптимизации
Если не хочется сортировать тяжёлые блины,
можно использовать для решения этой задачи дополнительную память.
В этом случае алгоритм будет такой:
можно в любом порядке перебирать блины и, вытащив очередной
(допустим, с весом A), спрашивать: «А есть ли у вас блин с весом - X−A?».
Когда консультант ответит «Да, есть такой» — можно оставить себе текущий блин,
взять тот, что с весом − X−A, и пойти заниматься.
Для решения задачи можно использовать вспомогательную структуру,
которая называется «структура данных поиска».
Она умеет быстро наполняться содержимым и эффективно отвечать на вопросы
вроде «Есть ли у тебя элемент Y?».
Такой структурой может служить set, map или dict.
Алгоритм, применяющий структуру данных поиска, может выглядеть так:
"""
from typing import List, Tuple, Optional


def twosum_extra_ds(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for A in arr:
        Y = target_sum - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.


def read_input_extra_ds() -> Tuple[List[int], int]:
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


arr, target_sum = read_input_extra_ds()
print_result(twosum_extra_ds(arr, target_sum))
