"""
Объединение двух списков
с чередованием по индексу
и сохранением очередности.
"""
from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
	"""
	Создаем пустой список
	По очереди добавляем в него через индекс значения.
	:param a:
	:param b:
	:return:
	"""
	c = []
	y = 0
	for i in b:
		c.append(a[y])
		y = 1 + y
		c.append(i)

	return c


def read_input() -> Tuple[List[int], List[int]]:
	"""
	Функция считывания данных ввода
	и занесения их в списки a и b.
	:return:
	"""
	a = list(map(int, input().strip().split()))
	b = list(map(int, input().strip().split()))
	return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
