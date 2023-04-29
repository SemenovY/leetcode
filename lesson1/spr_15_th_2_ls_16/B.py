"""
B. Чётные и нечётные числа
На экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.
Программу, которая по трём числам определяет, выиграл игрок или нет.
"""


def check_parity(a: int, b: int, c: int) -> bool:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return True
    if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
        return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
