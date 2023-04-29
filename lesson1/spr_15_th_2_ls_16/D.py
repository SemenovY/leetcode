"""
Задача найти в списке n числа, значение которых строго больше,
чем значение соседних с ним чисел слева и справа.
Под хаотичностью погоды за n дней служба понимает количество дней,
в которые температура строго больше, чем в день до (если такой существует)
и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха
составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись
описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды
за этот период.
Заметим, что если число показаний n=1, то единственный день будет хаотичным.
"""
from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    """Здесь реализация вашего решения"""
    day = []
    if len(temperatures) == 1:
        return 1

    try:
        if temperatures[0] > temperatures[1]:
            day.append(temperatures[0])
    except Exception:
        pass

    if temperatures[-1] > temperatures[-2]:
        day.append(temperatures[-1])

    for i in (range(1, len(temperatures) - 1)):
        try:
            if temperatures[i-1] < temperatures[i]:
                if temperatures[i+1] < temperatures[i]:
                    day.append(temperatures[i])
        except Exception:
            pass

    return len(day)


def read_input() -> List[int]:
    """
    Формат ввода
    В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105.
    Во второй строке даны n целых чисел, значения темп. в каждый из n дней.
    Значения температуры не превосходят 273 по модулю.
    Формат вывода
    Выведите единственное число — хаотичность за данный период.
    """
    n = int(input('Введите кол-во дней: '))
    temperatures = list(map(int, input('Введите значения температуры: ').strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
