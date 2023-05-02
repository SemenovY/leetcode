"""
Алгоритм проверяет, будет ли фраза палиндромом.
Учитываются только буквы и цифры,
заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.
"""
import re


def is_palindrome(line: str) -> bool:
    """
    Логика проверки фразы на палиндром.
    Формат ввода
    В единственной строке записана фраза или слово.
    Буквы могут быть только латинские.
    Длина текста не превосходит 20000 символов.
    Фраза может состоять из строчных и прописных латинских букв,
    цифр, знаков препинания.
    Формат вывода
    Выведите «True», если фраза является палиндромом, и «False», если нет.
    :param line:
    :return:
    """
    altered_string = ''.join(re.sub(r'[^\w\s]', '', line).lower().strip().split())

    if altered_string == altered_string[::-1]:
        return True
    else:
        return False


print(is_palindrome(input()))
