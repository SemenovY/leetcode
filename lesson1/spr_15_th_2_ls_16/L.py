"""
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и
добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.
Формат ввода
На вход подаются строки s и t, разделённые переносом строки.
Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
Формат вывода
Выведите лишнюю букву.
"""
from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    """
    переводим в список
    сортируем
    сравниваем и удаляем совпадения
    :param shorter:
    :param longer:
    :return:
    """
    shorter1 = list(map(str, shorter))
    longer1 = list(map(str, longer))
    shorter1.sort()
    longer1.sort()
    for i in shorter1:
        if i in longer1:
            longer1.remove(i)
    result = longer1[0]

    return result


def read_input() -> Tuple[str, str]:
    """
    На вход подаются строки s и t, разделённые переносом строки.
    Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
    :return:
    """
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
