"""
Напишите программу, которая определяет,
будет ли положительное целое число степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4n,
где n – целое неотрицательное число.
Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.
Формат вывода
Выведите «True», если число является степенью четырёх,
 «False» –— в обратном случае.
"""


def is_power_of_four(number: int) -> bool:
    """
    Получаем на вход число
    прогоняем по циклу, проверяем по формуле.
    :param number:
    :return:
    """
    a = 4
    for n in range(0, number//a + 1):
        if a**n == number:
            return True
    else:
        return False


print(is_power_of_four(int(input())))