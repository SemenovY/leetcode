"""
Эта функция переводит целое число из десятичной системы в двоичную.
"""


def to_binary(number: int) -> str:
	"""
	Проверяем на ноль
	Затем по формуле делим на 2, собираем остаток
	Далее остаток в списке инвертируем
	Убираем все лишние знаки препинания
	:param number:
	:return:
	"""
	if number != 0:
		binary = []
		while number != 0:
			b, c = number // 2, number % 2
			number = b
			binary.append(c)
		binary = map(int, binary[::-1])
		binary = " ".join(list(map(str, binary)))
		binary = str(binary.replace(' ', ''))
		return binary
	return str(number)


def read_input() -> int:
	"""
	Считываем на вход с терминала число
	:return:
	"""
	return int(input().strip())


print(to_binary(read_input()))
